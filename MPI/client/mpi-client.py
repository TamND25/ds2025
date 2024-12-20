from mpi4py import MPI
import base64
import os

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Constants
BUFFER_SIZE = 1024

def client(filename):
    """Client function to send file data."""
    if not os.path.exists(filename):
        print(f"Client (Rank {rank}): Error: File '{filename}' not found!")
        comm.send("DONE", dest=0, tag=0)
        return

    file_size = os.path.getsize(filename)
    metadata = {"filename": os.path.basename(filename), "size": file_size, "source": rank}

    print(f"Client (Rank {rank}): Sending file '{filename}' to server...")

    # Send metadata to server
    comm.send(metadata, dest=0, tag=0)

    # Send file in chunks
    with open(filename, "rb") as file:
        while chunk := file.read(BUFFER_SIZE):
            comm.send(base64.b64encode(chunk), dest=0, tag=1)

    print(f"Client (Rank {rank}): File '{filename}' sent successfully.")

if rank != 0:
    # Each client prompts for a file to send
    filename = input(f"Client (Rank {rank}): Enter the file name to send: ").strip()
    client(filename)

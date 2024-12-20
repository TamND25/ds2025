from mpi4py import MPI
import base64
import os

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Constants
OUTPUT_DIR = "received_files/"
BUFFER_SIZE = 1024

def server():
    """Server function to receive file data."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Loop to handle multiple client file transfers
    while True:
        print(f"Server (Rank {rank}): Waiting to receive file data...")
        file_metadata = comm.recv(source=MPI.ANY_SOURCE, tag=0)

        if file_metadata == "DONE":
            print(f"Server (Rank {rank}): All transfers complete. Exiting.")
            break

        filename = file_metadata["filename"]
        file_size = file_metadata["size"]
        source = file_metadata["source"]
        output_file = os.path.join(OUTPUT_DIR, f"received_from_rank_{source}_{filename}")

        print(f"Server (Rank {rank}): Receiving file '{filename}' from Rank {source}...")

        # Receive file in chunks
        with open(output_file, "wb") as file:
            received_bytes = 0
            while received_bytes < file_size:
                data_chunk = comm.recv(source=source, tag=1)
                file.write(base64.b64decode(data_chunk))
                received_bytes += len(base64.b64decode(data_chunk))

        print(f"Server (Rank {rank}): File '{filename}' saved as '{output_file}'.")

if rank == 0:
    server()

import socket

# Set up
filename = input("Input filename: ")
host="0.0.0.0"
port=12345
buffer_size=1024

# Initialize connection with server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print(f"Set up connection with {host}:{port}")

# Send file
with open(filename, "rb") as file:
    while True:
        data = file.read(buffer_size)
        if not data:
            break
        client_socket.sendall(data)

print("Sent successfully.")

# Close connection
client_socket.close()
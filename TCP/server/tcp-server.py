import socket

# Set up
host="0.0.0.0"
port=12345
buffer_size=1024
output_file="file_received.txt"

# Initialize server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server is waiting on {host}:{port}...")

# Connect with client
client_connection, client_address = server_socket.accept()
print(f"Connected with {client_address}")

# Receive file
with open(output_file, "wb") as file:
    while True:
        data = client_connection.recv(buffer_size)
        if not data:
            break
        file.write(data)

print("File received")

# Close connection and server
client_connection.close()
server_socket.close()

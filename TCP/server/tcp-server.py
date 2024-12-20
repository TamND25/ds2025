import socket

def setup_server(host="0.0.0.0", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is waiting on {host}:{port}...")
    return server_socket

def receive_file(server_socket, output_file="file_received.txt", buffer_size=1024):
    client_connection, client_address = server_socket.accept()
    print(f"Connected with {client_address}")

    with open(output_file, "wb") as file:
        while True:
            data = client_connection.recv(buffer_size)
            if not data:
                break
            file.write(data)

    print("File received")
    client_connection.close()
    server_socket.close()

server_socket = setup_server()
receive_file(server_socket, output_file="received_file.txt")

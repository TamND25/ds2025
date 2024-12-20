import socket

def setup_client(host="0.0.0.0", port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Set up connection with {host}:{port}")
    return client_socket

def send_file(client_socket, filename, buffer_size=1024):
    with open(filename, "rb") as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            client_socket.sendall(data)

    print("Sent successfully.")
    client_socket.close()

filename = 'text.txt'
client_socket = setup_client()
send_file(client_socket, filename)
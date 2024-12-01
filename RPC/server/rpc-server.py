from xmlrpc.server import SimpleXMLRPCServer
import base64

# Set up
host = "0.0.0.0"
port = 12345
output_file = "file_received.txt"

# Function to receive file
def save_file(encoded_data):
    with open(output_file, "wb") as file:
        file.write(base64.b64decode(encoded_data))
    return "File received"

# Initialize server
server = SimpleXMLRPCServer((host, port))
print(f"RPC Server is running on {host}:{port}...")
server.register_function(save_file, "save_file")

# Run the server
server.serve_forever()

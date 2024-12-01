import xmlrpc.client
import base64

# Set up
host = "http://0.0.0.0"
port = 12345
server_url = f"{host}:{port}"
filename = input("Input filename: ")

# Initialize client
client = xmlrpc.client.ServerProxy(server_url)

# Encode file data
with open(filename, "rb") as file:
    encoded_data = base64.b64encode(file.read()).decode()

# Send file to server
response = client.save_file(encoded_data)
print(response)

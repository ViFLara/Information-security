import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket successfully created!")

host = "localhost"
port = 5432

s.bind((host, port))
message = "\nServer: Hello Client!"

while 1:  # while is true
    data, address = s.recvfrom(4096)

    if data:  # if has data
        print("Sending message server...")
        s.sendto(data + (message.encode()), address)

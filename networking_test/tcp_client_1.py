import socket


TCP_IP = '10.227.10.53' # '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024 # A common default?

message = "Hello Sabastian!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendto(message.encode(), (TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

print("data received: ", data.decode())


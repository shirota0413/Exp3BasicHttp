import socket
import requests

#ip = socket.gethostbyname("http://13.114.69.220/hi")
IP = "13.114.69.220"
PORT = 80
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP,PORT))
    print(s.recv(BUFFER_SIZE).decode("utf-8"))
    print(s.recv(BUFFER_SIZE).decode("utf-8"))


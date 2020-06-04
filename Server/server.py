import socket

host = socket.gethostname()
PORT = 80
BUFFER_SIZE = 2048
count = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,PORT))
    s.listen(1)
    while True:
        connection, client = s.accept()
        print(connection,client)
        try:
            header = 'HTTP/1.1 200 OK\n' + 'Hello: BasicHTTP!\n' + 'Content-Length: 13\n' + 'Content-Type: text/plain; charset=utf-8\n'
            body = (socket.gethostbyname(host) + '\n').encode('utf8')

            connection.send(header.encode('utf8'))

            connection.send(body)

            data = connection.recv(BUFFER_SIZE)
            connection.send(data.upper())
        finally:
            connection.close()
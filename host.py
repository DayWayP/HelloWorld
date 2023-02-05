import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "151.80.167.71"
port = 4444

s.bind((host, port))
s.listen(1)
print("Идёт подключение...")

conn, addr = s.accept()
print("Подключено к ", addr)
import socket

# Server port
SERVER_PORT = 3000
# Server host(IPv4 address)
SERVER_HOST = "192.168.189.129"

# Tao mot the hien cua socket voi 2 tham so:
# * socket.AF_INET: dai dien cho dia chi IPv4
# * socket.SOCK_STREAM: loai socket la TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# De may server chi giao tiep cac may client 
# ket noi toi dia chi IP: 192.168.189.129
server.bind((SERVER_HOST, SERVER_PORT))
# Cho phep server chap nhan ket noi
server.listen(5)

# Tao ket noi voi may client
# * addr: dia chi IPv4 cua client
# * conn: la mot object socket moi dung de
# gui va nhan du lieu tren ket noi nay
conn, addr = server.accept()

print("Connect by ", addr)

while True:
    # Nhan du lieu gui tu client
    data = conn.recv(1024)
    # Tao du lieu phan hoi lai cho client
    response = "Hello " + data.decode("utf-8")
    if not data:
        break
    # Gui phan hoi lai cho client
    conn.sendall(bytes(response, "utf-8"))
   # s.close()

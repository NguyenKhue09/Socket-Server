import socket
import ssl

HOST = "192.168.189.129"
PORT = 3000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Tuong tu client nhung duoc truyen them tham so server_side = true
# de xac dinh hanh vi la server
server = ssl.wrap_socket(
    server, server_side=True, keyfile="./server.key", certfile="./server.pem"
)

if __name__ == "__main__":
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        connection, client_address = server.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            messegeResponse = "Hello " + data.decode("utf-8")
            connection.send(bytes(messegeResponse, "utf-8"))
            print(f"Received: {data.decode('utf-8')}")
        connection.close()

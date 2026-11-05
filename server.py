import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print("[*] Server listening on 127.0.0.1:8080")
    
    while True:
        client_sock, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        request = client_sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        client_sock.send(b"ACK: Message received by central server")
        client_sock.close()

if __name__ == "__main__":
    run_server()

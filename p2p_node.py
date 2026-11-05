import socket
import threading

def handle_peer(client_socket):
    request = client_socket.recv(1024)
    print(f"\n[P2P Incoming] {request.decode('utf-8')}")
    client_socket.send(b"P2P ACK")
    client_socket.close()

def start_listener(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', port))
    server.listen(5)
    while True:
        client_sock, _ = server.accept()
        threading.Thread(target=handle_peer, args=(client_sock,)).start()

def connect_to_peer(target_port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', target_port))
    client.send(message.encode('utf-8'))
    response = client.recv(1024)
    print(f"[P2P Response] {response.decode('utf-8')}")
    client.close()

if __name__ == "__main__":
    import sys
    my_port = int(sys.argv[1])
    # Start background listener thread
    threading.Thread(target=start_listener, args=(my_port,), daemon=True).start()
    print(f"[*] P2P Node running and listening on port {my_port}")
    
    # Interactive prompt to send message to another peer port
    while True:
        target = input("Enter target peer port to send message to (or 'q' to quit): ")
        if target == 'q': break
        msg = input("Enter message: ")
        connect_to_peer(int(target), msg)

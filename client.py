import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    client.send(b"Hello from client node!")
    response = client.recv(1024)
    print(f"[*] Response from server: {response.decode('utf-8')}")
    client.close()

if __name__ == "__main__":
    run_client()

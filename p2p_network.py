import socket
import threading

def send_message(dest_ip, dest_port):
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((dest_ip, dest_port))
                s.sendall(message.encode())
            except ConnectionRefusedError:
                print("Connection refused. Make sure the peer is running.")
            except Exception as e:
                print(f"An error occurred: {e}")

def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    print(f"Received message: {data.decode()} from {addr[0]}")

if __name__ == "__main__":
    server_port = 12345
    dest_ip = input("Enter destination IP address: ")
    dest_port = int(input("Enter destination port number: "))
    
    server_thread = threading.Thread(target=start_server, args=(server_port,))
    server_thread.start()
    
    send_thread = threading.Thread(target=send_message, args=(dest_ip, dest_port))
    send_thread.start()

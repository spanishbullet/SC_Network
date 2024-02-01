import socket
import threading

def receive_message(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print('Server has exited the chat.')
            break
        print('Received from server: ' + data)

def send_message(client_socket):
    while True:
        message = input(" -> ")
        if message.lower().strip() == 'exit':
            client_socket.send(message.encode())
            break
        client_socket.send(message.encode())

def start_client():
    host = '192.168.0.204'  # Replace with the IP address of the machine running the server script
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    threading.Thread(target=receive_message, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == '__main__':
    start_client()

import socket

def start_client():
    host = '192.168.0.204'  # Replace with the IP address of the machine running the server script
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        if not data or data.lower() == 'exit':
            print('Server has exited the chat.')
            break
        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    start_client()

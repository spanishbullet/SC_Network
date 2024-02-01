import socket
import threading

def send_message(conn):
    while True:
        data = input(' -> ')
        if data.lower() == 'exit':
            conn.send(data.encode())
            break
        elif data.lower() == 'sendfile':
            filename = input("Enter the filename: ")
            f = open(filename,'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            f.close()
        else:
            conn.send(data.encode())


def send_message(client_socket):
    while True:
        message = input(" -> ")
        if message.lower().strip() == 'exit':
            client_socket.send(message.encode())
            break
        elif message.lower().strip() == 'sendfile':
            filename = input("Enter the filename: ")
            f = open(filename,'rb')
            l = f.read(1024)
            while (l):
                client_socket.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            f.close()
        else:
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
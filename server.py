import socket
import threading

def receive_message(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("User has exited the chat.")
            break
        print("Received from user: " + str(data))

def send_message(conn):
    while True:
        data = input(' -> ')
        if data.lower() == 'exit':
            conn.send(data.encode())
            break
        conn.send(data.encode())

def start_server():
    host = '0.0.0.0'
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    threading.Thread(target=receive_message, args=(conn,)).start()
    threading.Thread(target=send_message, args=(conn,)).start()

if __name__ == '__main__':
    start_server()

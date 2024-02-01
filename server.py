import socket

def start_server():
    host = '0.0.0.0'  # This will allow connections on all network interfaces
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("User has exited the chat.")
            break
        print("Received from user: " + str(data))

        data = input(' -> ')
        if data.lower() == 'exit':
            conn.send(data.encode())
            break
        conn.send(data.encode())


    conn.close()

if __name__ == '__main__':
    start_server()

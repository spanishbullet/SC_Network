import socket
import threading

def receive_message(conn):
    while True:
        data = conn.recv(1024)
        if not data or data.lower() == b'exit':
            print("User has exited the chat.")
            break
        with open('received_file', 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = conn.recv(1024)
                print(f'data={data}')
                if not data:
                    break
                f.write(data)
    print('Successfully got the file')

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

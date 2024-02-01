# Overview

The networking program I provided is a basic chat application using a client-server model. It’s written in Python and uses the built-in socket and threading libraries for network communication and concurrent execution, respectively.

To use this software, you need to start both the server and the client. Here’s how:

Server: Run the server script on the machine that you want to act as the server. The server will start listening for incoming connections on port 5000. When a client connects, the server will start two threads: one for receiving messages from the client and another for sending messages to the client.

Client: Run the client script on the machine that you want to act as the client. The client will connect to the server using the server’s IP address and port number. Similar to the server, the client will also start two threads: one for receiving messages from the server and another for sending messages to the server.

Once connected the server and client can send simple text back and forth by typing the desired text into the terminal and pressing enter. That text will apear in the terminal on the other end of the connection. Either the server or the client can type 'sendfile' and press enter to send a file. The user will be prompted to enter the file name and press enter. The file entered will be sent as text to the other end of the connection and will apear as a message and a new file will be created on the machine receiveing the file. Similairly either machine can type 'quit' and press enter. This will close the connection and notify the other end that the connection was terminated by the other machine.

The purpose of writing this software is to demonstrate a basic implementation of a chat application using a client-server model. It provides a simple way for two parties to communicate with each other over a network. The software also includes the ability to send files from one party to another. However, please note that this is a basic implementation and might not be suitable for a production environment. It lacks features like support for multiple clients, robust error handling, and security measures. If you plan to use this in a real-world application, you might want to consider adding these features.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The architecture used in this project is a client-server model. In this model, the server listens for connections and the client connects to the server. Once the connection is established, they can exchange messages back and forth.

The project uses the TCP protocol for communication. TCP, or Transmission Control Protocol, is a connection-oriented protocol that ensures reliable and ordered delivery of data, which is crucial for a chat application. The port number used in this project is 5000.

The format of the messages being sent between the client and server is a string of text. The text is encoded to bytes before being sent over the network using the send_message() function, and it’s decoded back into a string upon receipt using the receive_message() function. If the message is ‘sendfile’, the subsequent bytes sent are treated as the contents of a file. The file is received and written to disk by the receiver. The communication ends when either the client or server sends the string ‘exit’.

# Development Environment

Visual Studio Code (VS Code) is an excellent Integrated Development Environment (IDE) for this project due to its comprehensive features and benefits. It offers robust support for Python, the language used in this project, including features like IntelliSense, linting, debugging, code navigation, and formatting. Its rich ecosystem of extensions enhances the development experience, and its built-in Git support simplifies version control. VS Code’s integrated terminal allows you to run your Python scripts or start your server/client without leaving the IDE. Its powerful debugging tools allow for setting conditional breakpoints, stepping through your code, inspecting variables, and viewing the call stack. Furthermore, VS Code is highly customizable, allowing you to adjust the layout, theme, keyboard shortcuts, and preferences to suit your needs. Lastly, its cross-platform capability ensures that you can work on your project on any operating system. These features collectively make VS Code a highly recommended IDE for this project.

Python is used for this project because it is a high-level, interpreted, and dynamically-typed programming language known for its readability and simplicity. It’s an interpreted language, meaning it runs directly from the source code, converting it into an intermediate language which is then translated into machine language for execution. Python’s vast standard library supports a wide range of areas including internet protocols, string operations, web services tools, and operating system interfaces, reducing the amount of code that needs to be written. Python’s portability and extensibility make it suitable for coding portable graphical user interfaces, database access programs, web-based systems, and more. It can run on all modern operating systems through the same byte code.

The provided code uses two built-in Python libraries: socket and threading. The socket module provides access to the BSD socket interface, allowing for the creation of socket objects and handling these objects for network communication. It’s fundamental for any kind of network communication in Python. The threading module constructs higher-level threading interfaces on top of the lower-level _thread module. It allows for multiple operations to happen at the same time, making the chat interactive with both parties able to send and receive messages at any time. These libraries were chosen because they are built into Python, requiring no additional installation, and they provide the necessary functionality for creating a basic chat server.

# Useful Websites

* [Python Download](https://www.python.org/downloads/)
* [Python Sockets](https://docs.python.org/3/library/socket.html)
* [Python Threading](https://docs.python.org/3/library/threading.html)
* [VS Code](https://code.visualstudio.com/download)
* [TCP](https://www.fortinet.com/resources/cyberglossary/tcp-ip#:~:text=Transmission%20Control%20Protocol%20(TCP)%20is,data%20and%20messages%20over%20networks.)

# Future Work

* Ability to connect and message more than one client at a time.
* Improve asyncronous messaging to be faster.
* Improve error handling.
* Change which port youre using.
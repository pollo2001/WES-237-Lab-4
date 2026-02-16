import time
import socket

#this will be my MAC


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: 
# 1: Connect the socket (sock) to the <SERVER-IP> and choosen port <LISTENING-PORT>
sock.connect(('192.168.0.189', 12345))
# 2: Send the message "Hello world!\n"
message = "Hello world!\n"
sock.send(message.encode())
# 3: Close the socket
print("socket closed")
sock.close()

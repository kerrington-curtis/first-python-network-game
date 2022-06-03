# Assignment 5 - client side

# create socket object
import socket
s = socket.socket()

# set ip address and port number
ip = '127.0.0.1'
port = 54321

# bind ip and port
s.connect((ip, port))
print(s.recv(1024).decode())

myBool = True

while myBool:
    guess = input("Guess a number from 1-100: ")
    s.send(guess.encode())

    response = s.recv(1024).decode()
    print(response)

    if response == "You got it!":
        myBool = False

s.close()

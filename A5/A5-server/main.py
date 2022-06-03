# Assignment 5 - server side

# I used the following code to help with logic:
# https://github.com/SamuelKinnett/python-network-guessing-game/blob/master/multithreaded/guessing-game-server.py

# create socket object
import socket
import random
s = socket.socket()

# set ip address and port number
ip = '127.0.0.1'
port = 54321

# bind ip and port
s.bind((ip, port))
s.listen(1)
print("Listening for a connection")

# add loop to continuously listen for connection
while True:
    conn, addr = s.accept()
    print("User connection from " + str(addr))
    conn.send("You've connected to my server. Let's play a game!".encode())

    # set random number and boolean
    randNum = int(random.randrange(1, 100))
    print("Random number generated: " + str(randNum))
    myBool = True

    # start game
    while myBool:
        clientInput = int(conn.recv(1024).decode())
        print("Client guessed: " + str(clientInput))
        if clientInput == randNum:
            conn.send("You got it!".encode())
            myBool = False
        else:
            if clientInput > randNum:
                conn.send("Too high!".encode())
            elif clientInput < randNum:
                conn.send("Too low!".encode())
    conn.close()

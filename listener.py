#!/usr/bin/python3

import socket
import sys
import threading
import os


# HOST = ''   # Symbolic name, meaning all available interfaces
# PORT = int(sys.argv[1]) # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print ('Socket created')
# #Bind socket to local host and port
# try:
#     s.bind((HOST, PORT))
# except socket.error as msg:
#     print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
#     sys.exit()
# print ('Socket bind complete')
# #Start listening on socket
# s.listen(10)
# print ('Socket now listening on port:' + str(PORT))
# #now keep talking with the client
# while 1:
#     #wait to accept a connection - blocking call
#     conn, addr = s.accept()
#     print ('Connected with ' + addr[0] + ':' + str(addr[1]))
# s.close()


########################################################################

#1
def send_commands(conn):
    while True:
        cmd = input() + "\n"  # Added \n 
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
#2
bind_ip = ""
bind_port = 1337
serv_add = (bind_ip ,bind_port)
#3
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(serv_add)
server.listen(5)
print ("[*] listening on {}:{}".format(bind_ip,bind_port))
#4
conn,addr = server.accept()
print('accepted connection from {} and port {}'.format(addr[0],addr[1]))
print("enter the commands below")
#5
send_commands(conn)
conn.close()


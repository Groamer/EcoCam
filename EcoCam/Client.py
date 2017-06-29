#!/usr/bin/python

__author__ = 'Tom Remeeus'

import socket

def convertData(data):
    #convert data from byte code to string
    data = data.decode("utf-8")
    data = data.replace("|", "\n")
    
    return data

def main():
    #print messages
    print("Connecting to server...")
    
    #set server address and port
    address = "192.168.0.105"
    port = 11221
    
    #connect to server and receive data
    s= socket.socket()
    s.connect((address, port))
    data = s.recv(1024)
    s.close()
    
    #print messages
    print("Retrieved data from server.")
    
    #print data
    print(convertData(data))
    
main()
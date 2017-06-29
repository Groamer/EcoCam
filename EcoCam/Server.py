#!/usr/bin/python

__author__ = 'Tom Remeeus'

import array
import socket
import os

def getVideos():
    fileList = "List of stored videos on server:|"
    
    #get directory where EcoCam is stored
    dir = os.path.dirname(os.path.realpath(__file__))
    
    #scan directory for .avi files
    for file in os.listdir(dir):
        if file.endswith(".avi"):
            fileList = fileList + file + "|"
    
    return fileList

def main():
    #print messages
    print("Starting server...")
    
    #setup connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.0.105", 11221))
    s.listen(1)
    
    #print messages
    print("Server online.")
    
    while(True):
        #print messages
        print("Awaiting connection...")
        
        #receive client
        (client, (ip, port)) = s.accept()
        client.send(str.encode(getVideos()))
        client.close()
        
        #print messages
        print("Client connected, and data was sent")
    
main() 
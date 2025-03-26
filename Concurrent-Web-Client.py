# -*- coding: utf-8 -*-
"""
Created on Tue March  26 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Concurrent Web Client")
print(Fore.GREEN+font)

import socket

BUFFER_SIZE = 1024

# Function to create and start the client
def start_client():
    try:
        # Prompt user for server details
        server_ip = input("Enter the server IP address:")
        server_port = int(input("Enter the server port:"))
        
        # Create the socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        
        # Prompt user for the message to send
        message = input("Enter the message to send to the server:")
        
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))
        
        # Receive the server's response
        response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"Server responded: {response}")
        
        # Close the connection
        client_socket.close()
    
    except Exception as e:
        print(f"Error in client: {e}")

# Entry point to start the client
if __name__ == "__main__":
    start_client()

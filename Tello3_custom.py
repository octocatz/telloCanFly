#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
from time import sleep

host = ''
port = 9001
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


sent = sock.sendto(b'command', tello_address)
print ("command")
sent = sock.sendto(b'takeoff', tello_address)
print ("takeoff")
sleep(5)
sent = sock.sendto(b'forward 100', tello_address)
print ("forward 100")
sleep(5)
sent = sock.sendto(b'flip f', tello_address)
print ("flip f")
sleep(5)
sent = sock.sendto(b'back 100', tello_address)
print ("back 100")
sleep(5)
sent = sock.sendto(b'land', tello_address)

#recvThread create
'''
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        print (msg)
        #sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break

'''



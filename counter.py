#!/usr/bin/python

###################################
# tldr: move led in a square pattern
###################################

import math
from struct import *
import socket, sys
import time;
UDP_IP = "192.168.1.1"
UDP_PORT = 9002


# led to light up
dumb = 1

# socket to send on
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# move led functions
def goUp(dumb):
    dumb  = dumb << 16;
    sendIt(dumb)
    return dumb

def goDown(dumb):
    dumb = dumb >> 16;
    sendIt(dumb)
    return dumb

def goLeft(dumb):
    dumb = dumb << 1;
    sendIt(dumb)
    return dumb

def goRight(dumb):
    dumb = dumb >> 1;
    sendIt(dumb)
    return dumb

# send led enoding on socket
def sendIt(dumb):
    sock.sendto(pack("Q", dumb),(UDP_IP, UDP_PORT))
    time.sleep(0.1);

# move led around
def dance(dumb):
    dumb = goLeft(dumb)
    dumb = goLeft(dumb)
    dumb = goLeft(dumb)
    dumb = goUp(dumb)
    dumb = goUp(dumb)
    dumb = goUp(dumb)
    dumb = goRight(dumb)
    dumb = goRight(dumb)
    dumb = goRight(dumb)
    dumb = goDown(dumb)
    dumb = goDown(dumb)
    dumb = goDown(dumb)

def main():
    dance(dumb)

if __name__ == "__main__":
    while True:
       main()

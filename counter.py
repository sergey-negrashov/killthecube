#!/usr/bin/python

import math
from struct import *
import socket, sys
import time;
UDP_IP = "192.168.1.1"
UDP_PORT = 9002


dumb = 1
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def goUp(dumb):
    dumb  = dumb << 16;
    sock.sendto(pack("Q", dumb),(UDP_IP, UDP_PORT))
    time.sleep(0.1);
    return dumb

def goDown(dumb):
    dumb = dumb >> 16;
    sock.sendto(pack("Q", dumb),(UDP_IP, UDP_PORT))
    time.sleep(0.1);
    return dumb

def goLeft(dumb):
    dumb = dumb << 1;
    sock.sendto(pack("Q", dumb),(UDP_IP, UDP_PORT))
    time.sleep(0.1);
    return dumb
def goRight(dumb):
    dumb = dumb >> 1;
    sock.sendto(pack("Q", dumb),(UDP_IP, UDP_PORT))
    time.sleep(0.1); 
    return dumb

while True:
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

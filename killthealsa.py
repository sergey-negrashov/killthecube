#!/usr/bin/python
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio, time, audioop
import math
from struct import *
import socket, sys
from ctypes import c_longlong as ll
UDP_IP = "192.168.1.1"
UDP_PORT = 9002

# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is suficcient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(160)
counter = 0;
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sampleMax = -1000000;
sampleMin = 1000000;
dumb = 0;
while True:
    # Read data from device
    l,data = inp.read()
    if l:
        # Return the maximum of the absolute value of all samples in a fragment.
        sample = 0;
        for i in range(0,10):
            temp = math.log(audioop.max(data, 2))
            if(sample < temp):
                sample = temp;
         
        if sampleMax < sample:
            sampleMax = sample
        if sampleMin > sample:
            sampleMin = sample;

        if(sampleMax != sampleMin):
            dumb =  int(4*(sample - sampleMin)/(sampleMax - sampleMin))
        if dumb == 0:
            sock.sendto(pack("Q", 0x0),(UDP_IP, UDP_PORT)) 
            print "";
        elif dumb == 1:
            sock.sendto(pack("Q",0x000000000000FFFF),(UDP_IP, UDP_PORT)) 
            print "*";
        elif dumb == 2:
            sock.sendto(pack("Q",0x00000000FFFFFFFF),(UDP_IP, UDP_PORT))
            print "**";
        elif dumb == 3:
            sock.sendto(pack("Q",0x0000FFFFFFFFFFFF),(UDP_IP, UDP_PORT)) 
            print "***";
        else :
            sock.sendto(pack("Q",0xFFFFFFFFFFFFFFFF),(UDP_IP, UDP_PORT))
            print "****";
        counter += 1;
        print sampleMax - sampleMin
        if(counter > 100 and sampleMax - sampleMin > 3):
            sampleMax = -1000000;
            sampleMin = 1000000;
            counter = 0;

#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct
import argparse

from scapy.all import sendp, send
#from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP, Raw
from scapy.all import *
from GLB_header import GLB

iface = 'client-eth1'

def main():

#This script creates 3 packets with diferent ncon values to be sent to the backends
#I chose to fill the packet with random strings

    pkt1 =  Ether () / IP(dst='10.0.0.2') /  GLB(ncon=1)/ Raw(RandString(size=26))  
    pkt2 =  Ether () / IP(dst='10.0.0.2') /  GLB(ncon=2)/ Raw(RandString(size=26))
    pkt3 =  Ether () / IP(dst='10.0.0.2') /  GLB(ncon=3)/ Raw(RandString(size=26))
#Show protocol stack
    pkt1.show()
    pkt2.show()
    pkt3.show()
#Send packets
    sendp(pkt1, iface=iface)
    sendp(pkt2, iface=iface)
    sendp(pkt3, iface=iface)


if __name__ == '__main__':
    main()
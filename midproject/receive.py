#!/usr/bin/env python3
import argparse
import sys
import struct
import os

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, TCP, UDP, Raw
from scapy.layers.inet import _IPOption_HDR
from GLB_header import GLB

def get_if(host_iface):
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if host_iface in i:
            iface=i
            break;
    if not iface:
        print("Cannot find " + host_iface + " interface")
        exit(1)
    return iface

def handle_pkt(pkt):
        print("got a packet")
        pkt.show()
#        hexdump(pkt)
#        print "len(pkt) = ", len(pkt)
        sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host_iface', type=str, default="eth1", help='The host interface use')
    args = parser.parse_args()

    iface = get_if(args.host_iface)
    print(("sniffing on %s" % iface))
    sys.stdout.flush()

    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
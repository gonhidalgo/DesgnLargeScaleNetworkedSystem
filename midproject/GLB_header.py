#! /usr/bin/env python

# Set log level to benefit from Scapy warnings
import logging
logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)

from scapy.all import *

PROTO_GLB = 0x12

class GLB(Packet):
    name = "GBL Packet"
    fields_desc = [ ShortField("ncon", 1),
    ]

def make_test():
    return Ether()/IP()/GLB(ncon=1)

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Test add-on v3.14")

bind_layers(IP, GLB, proto=PROTO_GLB)
#!/usr/bin/env python
import sys
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
conn.send_bytes(sys.argv[1])
print conn.recv_bytes()
conn.close()

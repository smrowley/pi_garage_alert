from multiprocessing.connection import Client

address = ('pi ip address', 6000)
conn = Client(address, authkey='secret password')
print conn.recv_bytes()
conn.close()

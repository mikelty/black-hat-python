#udp is connectionless so there's no connect like tcp.

import socket


target_host = "127.0.0.1"
target_port = 80

#create udp port
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#talk
client.sendto("XYZ", (target_host, target_port))
print client.recvfrom(4096)[0]
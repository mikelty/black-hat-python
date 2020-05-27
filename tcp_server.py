import socket
import threading


bind_ip = "0.0.0.0"
bind_port = 9999

#server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#a thraed for handling client
def handle_client(client_socket):
	request = client_socket.recv(1024)
	print "[*] Received: %s" % request
	client_socket.send("ACK!")
	client_socket.close()


#main client-server loop
while True:
	client, addr = server.accept()
	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()
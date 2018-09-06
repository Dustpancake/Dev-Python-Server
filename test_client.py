from socket import socket, AF_INET, SOCK_STREAM

def test():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(("localhost", 5790))
	chunk = sock.recv(4096)
	print("client got '{}'".format(chunk))

test()
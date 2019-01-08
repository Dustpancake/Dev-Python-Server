import threading

class client_thread(threading.Thread):
	def __init__(self, socket):
		self.socket = socket
		msg = "test"
		socket.send(msg.encode())
		msg = socket.recv(4096)
		print("server got {}".format(msg.decode()))

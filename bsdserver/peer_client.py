import threading

class client_thread(threading.Thread):
	def __init__(self, socket):
		self.socket = socket
		msg = "hello from server " + str(i)
		socket.send(msg.encode())

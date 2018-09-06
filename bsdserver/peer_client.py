import threading

class client_thread(threading.Thread):
	def __init__(self, socket):
		i = 0
		self.socket = socket
		msg = "hello from server " + str(i)
		socket.send(msg.encode())
		i+=1
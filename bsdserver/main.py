from socket import socket, AF_INET, SOCK_STREAM
from bsdserver.support import Config
import bsdserver.peer_client
from multiprocessing import Process, Queue
import importlib

class peer_to_peer(Process):
	def __init__(self):
		Process.__init__(self)
		self.daemon=True
		serversocket = socket(AF_INET, SOCK_STREAM)

		serversocket.bind(self._get_host_port())
		self.srvsocket = serversocket
		self.clients = {}

	def start(self):
		print("server starting at {}:{}".format(self.host, self.port))
		self.srvsocket.listen(5)
		while True:
			clientsocket, address = self.srvsocket.accept()
			print("connection from {}".format(address))
			self._attach(clientsocket, address)

	def _attach(self, csocket, addr):
		importlib.reload(bsdserver.peer_client)
		client_thread = bsdserver.peer_client.client_thread
		ct = client_thread(csocket)
		self.clients[addr] = ct

	def _get_host_port(self):
		c = Config()
		host = c.get("ServerAddress", "host")
		port = int(c.get("ServerAddress", "port"))
		self.host = host
		self.port = port
		return (host, port)

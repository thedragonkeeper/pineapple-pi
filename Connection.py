import socket
from datetime import datetime
import fcntl
import struct
from urllib.request import urlopen

class Connection(object):
	def __init__(self):
		self.onlinetext = "\u2714"
		self.interface = 'usb0'
		self.ip = ''

	def get_ip_address(self, ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,
			struct.pack('256s'.encode('utf-8'), ifname[:15].encode('utf-8'))
			)[20:24])

	def check_interface(self, dev):
		self.ip = self.get_ip_address(dev)
		self.interface = dev

	def is_connected(self):
		try:
			response = urlopen('http://www.example.com', timeout=10)
			self.onlinetext = "\u2714"
		except:
			self.onlinetext = "\u2717"

	def do_update(self, dev):
		self.check_interface(dev)
		self.is_connected()
		return str(self.ip),str(self.interface),self.onlinetext

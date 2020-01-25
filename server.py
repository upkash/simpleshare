#Server listens to recieve file 

import socket
import os
import sys

def startListen(port):
	s = socket.socket()
	s.bind(('0.0.0.0', port))
	print("Listening for a Connection")
	s.listen(1)
	while True:
		c, addr = s.accept()
		print("Connection from: " + addr[0])
		file = c.recv(1024)
		print("Recieving " + file " from " +addr[0])
	

		f = open(file, 'wb')
		while True:
			data = c.recv(1024)
			if not data:
				break
			f.write(data)
		print("From IP " + file)
		f.close()
	c.send("Thank you for using sockets")
	c.close()


def Main():
	startListen(1000)

if __name__ == '__main__':
	Main()

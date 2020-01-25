#client to send file and file name
import socket
import os 
import sys

def send_file(file_name, host, port):
	with socket.socket() as s:
		s.connect((host, port))
		s.send(file_name.encode('utf-8'))
		with open(file_name, 'rb') as f:
			s.sendall(f.read())


def Main():
	if len(sys.argv) != 4:
		usage()
		exit()
	send_file(sys.argv[1], socket.gethostbyname(sysargv[2]), int(sysargv[3]))
	exit()

if __name__ == '__main__':
	Main()
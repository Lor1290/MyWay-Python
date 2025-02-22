import socket, subprocess, threading
import time, sys

from colorama import Fore

class Main:
	
	@staticmethod
	def new_client(client, addr) -> object:
		while True:
			send_command = input(Fore.GREEN + "[+] ready to send: ")
			client.send(send_command.encode())
			
			ret_command = client.recv(1024)
			print(Fore.GREEN + "[+] Command sent correctly!")
		client.close()

	@staticmethod
	def enstablish() -> None:
		port, host = 0, 0

		dec = ''
		while dec != 'y':
			host = input(Fore.WHITE + "[s] Select the host ip: ")
			dec = input(Fore.YELLOW + "[?] are you sure you want to use: {host} [y/n]: ").lower().strip()
		
		dec = ''
		while dec != 'y':
			port = input(Fore.WHITE + "[s] Select the port id: " )
			dec = input( Fore.YELLOW + f"[?] are you sure you want to use: {port} [y/n]: ").lower().strip()
	

		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind((host, int(port)))
		print(Fore.GREEN + f"[+] server started at port {port}")
		
		server_socket.listen(10)
		print("[-] Server is now listening...")

		while True:
			conn, adress = server_socket.accept()
			print(Fore.GREEN + f"[+] connection recived from: {adress}")
			
			client_thread = threading.Thread(target = Main.new_client, args = (conn, adress))
			client_thread.start()

if __name__ == '__main__':
	start = Main()
	start.enstablish()

import os
import sys, socket, subprocess, threading

class Main: 
	
	@staticmethod	
	def new_client(client, addr):
		while True:
			msg = client.recv(1024)
			print(f"{addr} >> {msg}")

			msg = input(">>> ")
			client.send(msg.encode())
			
			out = client.recv(1024)
			for elem in out:
				print(f"{addr} >> {elem}")
			
		client.close()

	@staticmethod
	def enstablish() -> None:
		host = socket.gethostname()
		port = 8080

		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind((host, port))
		print(f"Server started of port {port}")
		
		server_socket.listen(10)
		print("Server now listenin...")		
		
		while True:	
			conn, adress = server_socket.accept()
			print(f"Connection from: {adress}")
			
			client_thread = threading.Thread(target=Main.new_client,args=(conn, adress))
			client_thread.start()
		server_socket.close()
		
if __name__ == '__main__':
	start = Main()
	start.enstablish()

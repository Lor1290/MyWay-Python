import socket, subprocess

class Main:

	@staticmethod
	def connect():
		host = socket.gethostname()
		port = 8080

		client_socket = socket.socket()
		client_socket.connect((host, port))

		message = input(">>> ")
		while message.lower().strip() != 'exit':
			client_socket.send(message.encode())
			
			try:
				data = client_socket.recv(1024).decode()
				good_data = subprocess.run(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				
				output = good_data.stdout.decode().splitlines()
				print(output)
				for line in output:
					client_socket.send(line.encode())			
		
			except ConnectionResetError:
				print(f"Connection with port: {port} closed. exiting...")
				break
			
			message = input(">>> ")
		client_socket.close()

if __name__ == '__main__':
	start = Main()
	start.connect()

import socket
import subprocess

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "192.168.43.141"
port = 2222

s.bind( (ip, port))
s.listen()

csession, caddr = s.accept()

location = csession.recv(20).decode()
print(location)

if location == "local":

	while True:
		data = csession.recv(200).decode()
		
		if int(data) == 1:	
		
			output = subprocess.getoutput("date")
			csession.send(output.encode())
			print(output)
		elif int(data) == 2:
		
			output = subprocess.getoutput("cal")
			csession.send(output.encode())
			print(output)
		#elif int(data) == 3:
			#output = subprocess.getoutput("date")
			#csession.send(output.encode())
			#print(output)
		else:
			csession.send(print("Invalid Choice.Please enter again....!!".encode()))

elif location == "remote":
	
	remote_ip = csession.recv(50).decode()
	while True:
	
		data = csession.recv(200).decode()
		
		if int(data) == 1:	
		
			output = subprocess.getoutput("ssh {} date".format(remote_ip))
			csession.send(output.encode())
			print(output)
		elif int(data) == 2:
		
			output = subprocess.getoutput("ssh {} cal".format(remote_ip))
			csession.send(output.encode())
			print(output)
		else:
			csession.send(print("Invalid Choice.Please enter again....!!".encode()))
else:
	print("Not supported")


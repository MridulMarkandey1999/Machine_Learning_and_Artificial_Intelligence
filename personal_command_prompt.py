#make you own command prompt
#client-side-code
import socket


s = socket.socket()

server_ip ="192.168.43.141"
server_port =2222
s.connect((server_ip, server_port))

while True:
    cmd = input("[root@localhost ~]# ")
    cmd = cmd.encode()
    s.send(cmd)
    output = s.recv(200).decode()
    print(output)

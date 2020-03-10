import socket


s = socket.socket()

server_ip ="192.168.43.141"
server_port =2222
s.connect((server_ip, server_port))

location = input("Enter location (local/remote): ")
print(location)
location = location.encode()
s.send(location)

if location.decode() == "local":
    while True:
        print(""""
            Press 1: to date
            Press 2: to calendar
            """)

        cmd = input("Enter your choice: ")
        cmd = cmd.encode()
        s.send(cmd)
        output = s.recv(200).decode()
        print(output)
elif location.decode() == "remote":
    remote_ip = input("Enter remote ip: ")
    remote_ip = remote_ip.encode()
    s.send(remote_ip)
    #remote_password = input("Enter password for remote system: ")
    #remote_password = remote_password.encode()
    #s.send(remote_password)
    while True:
        print(""""
            Press 1: to date
            Press 2: to calendar
            """)

        cmd = input("Enter your choice: ")
        cmd = cmd.encode()
        s.send(cmd)
        output = s.recv(200).decode()
        print(output)
else:
    print("Not Supported")
        

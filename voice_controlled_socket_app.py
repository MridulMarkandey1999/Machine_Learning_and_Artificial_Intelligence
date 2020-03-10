import socket
import os
import speech_recognition as sr

s = socket.socket()

server_ip ="192.168.43.141"
server_port =2223
s.connect((server_ip, server_port))

mic = sr.Microphone()
rec = sr.Recognizer()


#location = input("Enter location (local/remote): \n")
with mic as source:
    #os.system("echo Enter Location (local/remote): | festival --tts")
    print("Enter Location (local/remote): ",end='')
    audio = rec.listen(source)
    location = rec.recognize_google(audio)
    print(location)
#print(location)
location = location.encode()
s.send(location)

if location.decode() == "local":
    while True:
        
        print(""""
            Press 1: to date
            Press 2: to calendar
            """)

        #cmd = input("Enter your choice: ")
        with mic as source:
            #os.system("echo Enter your choice: | festival --tts")
            print("Enter your choice: ", end='')
            audio = rec.listen(source)
            cmd = rec.recognize_google(audio)
            print(cmd)
        cmd = cmd.encode()
        s.send(cmd)
        output = s.recv(200).decode()
        print(output)
elif location.decode() == "remote":
    #os.system("echo Enter remote IP: | festival --tts")
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

        #cmd = input("Enter your choice: ")
        with mic as source:
                #os.system("echo Enter your choice: | festival --tts")
                print(" Enter your choice: ", end='')
                audio = rec.listen(source)
                cmd = rec.recognize_google(audio)
                print(cmd)
        cmd = cmd.encode()
        s.send(cmd)
        output = s.recv(200).decode()
        print(output)
else:
    #os.system("echo not supported sir | festival --tts")
    print("Not Supported sir")

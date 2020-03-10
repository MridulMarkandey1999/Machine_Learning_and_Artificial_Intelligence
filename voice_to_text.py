#Program to recognize voice and  convert to text
import socket
import speech_recognition as sr

#s = socket.socket()

#server_ip ="192.168.43.141"
#server_port =2222
#s.connect((server_ip, server_port))

mic = sr.Microphone()
rec = sr.Recognizer()

with mic as source:
    print("say: ")
    audio = rec.listen(source)
    text = rec.recognize_google(audio)
    print(text)
    

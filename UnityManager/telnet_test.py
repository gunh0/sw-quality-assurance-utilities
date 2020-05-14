import getpass
import sys
import telnetlib

print('---------------------------TELNET TESTING START---------------------------')

HOST = "192.168.155.183"    # Redhat 7.3
user = "test04"
password = "1qa2ws3ed$"
port = "23"

telnet = telnetlib.Telnet(HOST, port)
response = telnet.read_until(b"login: ")
print(response)

telnet.write(user.encode('ascii') + b"\n")
telnet.read_until(b"Password: ")
response = telnet.write(password.encode('ascii') + b"\n")
print(response)

telnet.write(b"hostnamectl\n")
telnet.write(b"exit\n")
print(telnet.read_all())

print('---------------------------TELNET TESTING END---------------------------')

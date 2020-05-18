import getpass
import sys
import telnetlib

from UserInfo import UserInformation

print('---------------------------TELNET TESTING START---------------------------')

enter = UserInformation()
HOST = "192.168.155.183"    # Redhat 7.3
user = enter.username()
print(user)
password = enter.password()
print(password)
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

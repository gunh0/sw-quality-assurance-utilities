from ftplib import FTP
from UserInfo import UserInformation

print('---------------------------FTP TESTING START---------------------------')
target_server = "192.168.155.183"  # Redhat 7.3
enter = UserInformation()
userid = str(enter.username())
print(userid)
pwd = str(enter.password())
print(pwd)

# Anonymous
print('Anonymous FTP ')
ftp = FTP(target_server)
ftp.login()
ftp.retrlines('LIST')
print(ftp.pwd())
ftp.quit()

# user
print('\nUser FTP ')
uftp = FTP(target_server)
uftp.login(userid, pwd)
print(uftp.pwd())
uftp.quit()

print('---------------------------FTP TESTING END---------------------------')

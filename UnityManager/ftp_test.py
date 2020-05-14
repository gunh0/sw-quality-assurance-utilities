from ftplib import FTP

print('---------------------------FTP TESTING START---------------------------')
target_server = "192.168.155.183"  # Redhat 7.3
userid = "test04"
pwd = "1qa2ws3ed$"

ftp = FTP(target_server)
ftp.login()
ftp.retrlines('LIST')
ftp.quit()

uftp = FTP(target_server)
uftp.login(userid, pwd)
uftp.retrlines('LIST')
uftp.quit()

print('---------------------------FTP TESTING END---------------------------')

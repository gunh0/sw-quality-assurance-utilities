import paramiko
 
print('---------------------------SSH TESTING START---------------------------')
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
server = "192.168.155.183"  # Redhat 7.3 
user = "test04"  
pwd = "1qa2ws3ed$"
 
cli.connect(server, port=22, username=user, password=pwd)
stdin, stdout, stderr = cli.exec_command("hostnamectl")
lines = stdout.readlines()
print(''.join(lines))
stdin, stdout, stderr = cli.exec_command("ls -la")
lines = stdout.readlines()
print(''.join(lines))
 
cli.close()
print('---------------------------SSH TESTING END---------------------------')
### Simple Python code for internal network access testing

```powershell
> pip install virtualenv
> virtualenv venv		// virtualenv 'name'
> .\venv\Scripts\Activate
(venv) > python -m pip install -r requirements.txt
```

<br/>

### telnet

- Success

```
---------------------------TELNET TESTING START---------------------------
b'\r\nKernel 3.10.0-514.el7.x86_64 on an x86_64\r\nrhel73agent login: '
None
b'\r\nhostnamectl\r\nexit\r\nLast login: Thu May 14 01:58:07 from ::ffff:192.168.120.168\r\n-bash-4.2$ hostnamectl\r\n   Static hostname: rhel73agent\r\n         Icon name: computer-vm\r\n           Chassis: vm\r\n        Machine ID: b7bc1e5e2aed476c9efb76e4a7e6acfe\r\n           Boot ID: d4d65f88fe2c4d0897f1f47b959ed955\r\n    Virtualization: vmware\r\n  Operating System: Red Hat Enterprise Linux Server 7.3 (Maipo)\r\n       CPE OS Name: cpe:/o:redhat:enterprise_linux:7.3:GA:server\r\n            Kernel: Linux 3.10.0-514.el7.x86_64\r\n      Architecture: x86-64\r\n-bash-4.2$ exit\r\nlogout\r\n'
---------------------------TELNET TESTING END---------------------------
```

- Failure

```
---------------------------TELNET TESTING START---------------------------
b'\r\nKernel 3.10.0-514.el7.x86_64 on an x86_64\r\nrhel73agent login: '
None
b''
---------------------------TELNET TESTING END---------------------------
```

<br/>

### ftp

- Success

```
---------------------------FTP TESTING START---------------------------
Anonymous FTP
drwxr-xr-x    2 0        0               6 Jun 23  2016 pub
/

User FTP
/home/test04
---------------------------FTP TESTING END---------------------------
```

- Failure

```
---------------------------FTP TESTING START---------------------------
Anonymous FTP
drwxr-xr-x    2 0        0               6 Jun 23  2016 pub
/

User FTP
Traceback (most recent call last):
  File ".\ftp_test.py", line 19, in <module>
    uftp.login(userid, pwd)
  File "c:\python\python38-32\lib\ftplib.py", line 403, in login
    resp = self.sendcmd('PASS ' + passwd)
  File "c:\python\python38-32\lib\ftplib.py", line 275, in sendcmd
    return self.getresp()
  File "c:\python\python38-32\lib\ftplib.py", line 238, in getresp
    resp = self.getmultiline()
  File "c:\python\python38-32\lib\ftplib.py", line 224, in getmultiline
    line = self.getline()
  File "c:\python\python38-32\lib\ftplib.py", line 212, in getline
    raise EOFError
EOFError
```

<br/>

### ssh

- Success

```
---------------------------SSH TESTING START---------------------------
   Static hostname: rhel73agent
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b7bc1e5e2aed476c9efb76e4a7e6acfe
           Boot ID: d4d65f88fe2c4d0897f1f47b959ed955
    Virtualization: vmware
  Operating System: Red Hat Enterprise Linux Server 7.3 (Maipo)
       CPE OS Name: cpe:/o:redhat:enterprise_linux:7.3:GA:server
            Kernel: Linux 3.10.0-514.el7.x86_64
      Architecture: x86-64

total 4
drwxr-xr-x   4 test04 users  56 May 14 00:48 .
drwxr-xr-x. 13 root   root  156 May 14 00:49 ..
-rw-------   1 test04 users 299 May 14 00:49 .bash_history
drwxr-xr-x   3 test04 users  18 May 14 00:43 .cache
drwxr-xr-x   3 test04 users  18 May 14 00:49 .config

---------------------------SSH TESTING END---------------------------
```

- Failure

```
---------------------------SSH TESTING START---------------------------
Traceback (most recent call last):
  File ".\ssh_test.py", line 11, in <module>
    cli.connect(server, port=22, username=user, password=pwd)
...
paramiko.ssh_exception.AuthenticationException: Authentication failed.
```

<br/>
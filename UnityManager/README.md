```powershell
> pip install virtualenv
> virtualenv venv		// virtualenv 'name'
> .\venv\Scripts\Activate
(venv) > python -m pip install -r requirements.txt
```

<br/>

### ssh

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

```
---------------------------SSH TESTING START---------------------------
Traceback (most recent call last):
  File ".\ssh_test.py", line 11, in <module>
    cli.connect(server, port=22, username=user, password=pwd)
...
paramiko.ssh_exception.AuthenticationException: Authentication failed.
```
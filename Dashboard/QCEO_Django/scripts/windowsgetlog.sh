#!/usr/bin/expect -f
set timeout 30
set host [lindex $argv 0]
set id [lindex $argv 1]
set password [lindex $argv 2]
set logpath [lindex $argv 3]
set logname [lindex $argv 4]
spawn telnet $host
expect -re "login"
send "$id\r"
expect -re "assword"
send "$password\r"
expect -re "C:\Users\Administrator>"
send "if exist \"$logpath$logname\" start copy \"$logpath$logname\" C:\\FTP\r" 
expect -re "C:\Users\Administrator>"
send "exit\r"
spawn ftp $host
expect -re "Name"
send "$id\r"
expect -re "assword:"
send "$password\r"
expect -re "ftp>"
send "get $logname /home/qceo/QCEO/agentlogs/$logname\r"
expect -re "ftp>"
send "bye\r"
interact

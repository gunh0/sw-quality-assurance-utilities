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
send "if not exist \"$logpath\" start md \"$logpath\"\r" 
expect -re "C:\Users\Administrator>" 
send "if not exist \"$logpath$logname\" start type NUL > \"$logpath$logname\"\r"
expect -re "C:\Users\Administrator>"
send "exit\r"
interact

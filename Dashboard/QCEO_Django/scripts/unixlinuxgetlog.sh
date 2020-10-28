#!/usr/bin/expect
set idNhost [lindex $argv 0]
set password [lindex $argv 1]
set logpath [lindex $argv 2]
set logname [lindex $argv 3]
spawn scp $idNhost:$logpath$logname /home/qceo/QCEO/agentlogs/
expect -re "Password"
send "$password\r"
interact
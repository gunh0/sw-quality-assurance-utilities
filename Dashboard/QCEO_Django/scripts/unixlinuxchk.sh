#!/usr/bin/expect -f
set idNhost [lindex $argv 0]
set password [lindex $argv 1]
set logpath [lindex $argv 2]
set logname [lindex $argv 3]
spawn bash -c "ssh $idNhost bash -s < /home/qceo/QCEO/scripts/chklogfile.sh $logpath $logname"
expect -re "assword"
send "$password\r"
interact

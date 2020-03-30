#!/bin/sh
if [ `id | grep "uid=0"| wc -l` -eq 0 ] ; then
	echo "[-] Need 'root' Permission"
	exit
fi

if test -d $1 ; then
	echo "[-] Exist Dir"
	if test -e $1$2 ; then
		echo "[-] Exist Log"
	else
		`touch $1$2`
		echo "[-] Create Log"
	fi
else
	echo "[-] No Dir"
	`mkdir $1`
	`touch $1$2`
	echo "[-] Create Dir, Log"
fi

exit 0
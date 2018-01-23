#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo 'you need to put in two args $1 = amount of da pings $2 = ip'
	exit
fi

i=0

while [[ $i -lt $1 ]]; do
	echo $i
	ping -q $2 &
	i=$[$i+1]
done
echo ready for you to be done?
read y

killall ping

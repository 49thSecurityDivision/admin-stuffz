#!/bin/bash

xrandr --output eDP1 --mode 1920x1080
xrandr --setprovideroutputsource 1 0
xrandr --setprovideroutputsource 2 0
sleep 3
xrandr --output DVI-I-2-2 --right-of eDP1 --auto
xrandr --output DVI-I-1-1 --right-of DVI-I-2-2 --auto
sleep 3
#xrandr --output DVI-I-1-1 --rotate left
feh --randomize --bg-fill /home/elrey/pictures/background-pics/*

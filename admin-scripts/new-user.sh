#!/bin/bash

# used to add users to our pi audio server

# input validation
if [[ $# -ne 1 ]]; then
	echo "You had one job...username"
	exit
fi

# adding a user creating a home directory
# giving them bash as default shell and
# adding to audio group to play music on pi
sudo useradd -g audio -m -s /bin/bash $1

# copies a file we have all the commands
sudo cp ~/MUSIC_CHEAT_SHEET /home/$1/

# changing it to their user ownage
sudo chown $1:$1 /home/$1/MUSIC_CHEAT_SHEET

# using their user to create a .ssh/authorized_keys
# file to ensure they will be able to read it
sudo -H -u $1 bash -c 'mkdir ~/.ssh'
sudo -H -u $1 bash -c 'vim ~/.ssh/authorized_keys'
exit

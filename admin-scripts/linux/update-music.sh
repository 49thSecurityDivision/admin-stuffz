#!/bin/bash

ls /home/ | grep -v pi | xargs -I {} sudo cp ~/MUSIC_CHEAT_SHEET /home/{}/

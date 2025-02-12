#!/bin/zsh

ssh pi@172.17.21.2 -f 'rm -rf /home/pi/Projects/Inverted-Maze/';

# Copy Inverted-Maze Directory to Raspberry Pi
#scp -pr /home/soft-dev/Documents/Inverted-Maze/ pi@172.17.21.2:/home/pi/Projects/Inverted-Maze/
rsync -av --exclude='.git' /home/soft-dev/Documents/Inverted-Maze/ pi@172.17.21.2:/home/pi/Projects/Inverted-Maze/

ssh pi@172.17.21.2 'sudo pkill -15 -f "python3 client.py"'

# Execute client.py
ssh pi@172.17.21.2 'cd /home/pi/Projects/Inverted-Maze/; python3 client.py'
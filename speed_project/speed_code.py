#!/usr/bin/python
#runs the speedtest-cli sh

import subprocess

with open('/home/pi/Documents/speedlog.txt','a+') as log_file:
	log_file.write('running the shell script \n')

subprocess.call(['./speedtest-simple.sh'])


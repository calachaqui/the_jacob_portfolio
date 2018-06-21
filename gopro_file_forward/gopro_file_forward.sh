#!/usr/bin/sh

##program: gopro file forward
##author: Calachaqui
##objective: move new files from gopro to an external hardrive
##notes: in developement

## check to see if gopro has been connected
Directory = $("/media/gopro")
if [ ! -d "$Directory" ]; then
	exit 0
fi
##check to see if external hardrive is connected
Directory = $("/media/canvio")
if [ ! -d "$Directory" ]; then
	exit 0
fi


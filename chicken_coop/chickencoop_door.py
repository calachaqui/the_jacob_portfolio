#!/usr/bin/python

import time, gpiozero, datetime

##check open variable to see if door is open
with open("//home//pi//python_scripts//chicken_coop//door_status.txt") as DS:
    door_stat = DS.read()

##Check the time of day
now = datetime.datetime.time(datetime.datetime.now())
print (now)

now_hour = now.strftime('%H')
print (now_hour)

#logic to open or shut the door
if now_hour < 12:#is it morning?
    if door_stat == 'close':#is the door still closed
        print ("reversing motor to open the door")
        with open("//home//pi//python_scripts//chicken_coop//door_status.txt","w") as DS:
            DS.write('open')
        #run reverse motor code
    else:
        print ("Uh oh, the door was already open")
else:#if it is evening
    if door_stat == 'close':
        print("Uh oh, the door was already closed")
    else:
        print("running motor to close the door")
        with open("//home//pi//python_scripts//chicken_coop//door_status.txt","w") as DS:
            DS.write('close')
        #run forward motor code
print("Door function is complete. See you Next time")

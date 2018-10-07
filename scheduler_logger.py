#!/usr/bin/env python
##testing this script to be a scheduled task
##script will write to a log the current
##date and time and maybe some other things
##

import datetime
#
right_now = datetime.datetime.now()
#form_date = right_now.strftime('%Y%m%d')
#
#with open('/home/pi/python_scripts/logged_dates.txt','a') as the_log:
#	the_log.write("today's date is %s\n" % form_date)

import pyowm

owm = pyowm.OWM('a9bd34ad88582d8e147c150249581f0b')  # You MUST provide a valid API key

# Search for current weather in Orem (US)
observation = owm.weather_at_place('Orem,us')
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
#print w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#print w.get_humidity()              # 87
orem_temp = w.get_temperature('fahrenheit')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print orem_temp['temp']
oct = orem_temp['temp']


## uncomment this section to write out to log
with open('/home/pi/compute/run_log.txt','a') as the_log:
       the_log.write(str(right_now)+"	"+str(oct)+"\n")


#orem utah observations
#observation_list = owm.weather_around_coords(40.29, 111.69)
#print observation_list

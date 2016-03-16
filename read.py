"""
read.py

Monitor a GPIO pin for changes
pouring is defined as the pin state has changed in the past 
"""
import datetime
import RPi.GPIO as GPIO
import requests
import syslog

#how long after inactivity to consider a pour complete
threshold = 0.100 #s
gpio_pin = 4

kegbot_api_key = '2517f7a093ac2f3ba2b05cbd16663a2f'
kegbot_url = 'http://beer.corp.dyn.com'
kegbot_api_path = '/api/taps/kegboard-8ae4b601.mattpi.flow0'

headers = {"X-Kegbot-Api-Key": kegbot_api_key}

boardRevision = GPIO.RPI_REVISION
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#initial state
changed = False
pouring = False
current = GPIO.input(gpio_pin)
lastChangeTime = datetime.datetime.today()
pourStartTime = datetime.datetime.today()
ticks = 0

syslog.syslog("Entering Loop")

#main loop from which you never escape
while True:
    loopStartTime = datetime.datetime.today()

    read = GPIO.input(gpio_pin)

    if current != read:
        changed = True
        current = read
       
        if pouring == False: #a pour just started
            syslog.syslog("pouring")
            pourStartTime = loopStartTime
            ticks = 0

        pouring = True
        lastChangeTime = loopStartTime
        ticks +=1
    else:
        changed = False
        d = loopStartTime - lastChangeTime
        if d.total_seconds()> threshold:
            if pouring == True: #a pour just ended
                p = loopStartTime - pourStartTime
                print ("Pour Completed {} sec {} tick".format(p.total_seconds(), ticks))
                syslog.syslog("poured {}".format(ticks))

                #setup and make API call recording pour
                if ticks> 100:
                    payload = {"ticks": ticks}
                    url = "{}/{}".format(kegbot_url, kegbot_api_path)

                    print("Making request {}".format(url))
                    r = requests.post(url, headers= headers, data= payload)
                    syslog.syslog(r.text)
                    if r.status_code != 200:
                        print("pour api call returned {}".format(r.status_code))
 
                
            pouring = False


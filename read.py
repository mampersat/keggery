"""
read.py

Monitor a GPIO pin for changes
pouring is defined as the pin state has changed in the past 
"""
import datetime
import RPi.GPIO as GPIO

#how long after inactivity to consider a pour complete
threshold = 0.100 #s
gpio_pin = 4

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

#main loop from which you never escape
while True:
    loopStartTime = datetime.datetime.today()

    read = GPIO.input(gpio_pin)

    if current != read:
        changed = True
        current = read
       
        if pouring == False: #a pour just started
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
                
            pouring = False


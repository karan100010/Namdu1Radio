import RPi.GPIO as GPIO
from gpiozero import LED, Button
from dualled import DualLED

import os

stop_audio_list=[i for i in os.listdir("/home/pi/Documents/Namdu1Radio/audio-alert/") if "stop" in i]
names=[]

for i in stop_audio_list:
    if "_" in i:
        names.append(i.split("_")[0])
    else:
        names.append(i.split(".")[0])

stop_audio=dict(zip(names,stop_audio_list))

chromium_playing=False
previousTime = False
but1n2_pressed = False
ret = "Hello"
radio = False
duration = 5
genplaypause = True
# flag to check if button is pressed and held for long time
longpress = False 
longpress2 = False
# flag to monitor if radio is on or off
nammaschoolradio = True
#Variable to start the radio at the begining automatically
cntr = True
#Variable to used to start/stop the radio on button press
playpause = False
#Flag to monitor pendrive state
penDet = False
#Categories play and pause flags
cat1playpause = False
cat2playpause = False
cat3playpause = False
cat4playpause = False
cat5playpause = False
cat6playpause = False
cat7playpause = False
cat8playpause = False
cat9playpause = False
cat10playpause = False
cat1preview = False
cat2preview = False
cat3preview = False
cat4preview = False
cat5preview = False
cat6preview = False
cat7preview = False
cat8preview = False
cat9preview = False
cat10preview = False
gencatpreview = False
# network verification variables
remote_server = "www.google.com"
local_server = "192.168.1.50"
recFileName = "record"
# setting folder paths
projectpath =  os.path.split(os.path.realpath(__file__))[0]
audioguidepath = projectpath + "/audio-alert"
previewaudioguidepath = projectpath + "/recordings"
#local categories .wav file save path
recordingpath1to9 = projectpath + "/recordings/cat"
recordingpathcat1 = projectpath + "/recordings/cat1"
recordingpathcat2 = projectpath + "/recordings/cat2"
recordingpathcat3 = projectpath + "/recordings/cat3"
recordingpathcat4 = projectpath + "/recordings/cat4"
recordingpathcat5 = projectpath + "/recordings/cat5"
recordingpathcat6 = projectpath + "/recordings/cat6"
recordingpathcat7 = projectpath + "/recordings/cat7"
recordingpathcat8 = projectpath + "/recordings/cat8"
recordingpathcat9 = projectpath + "/recordings/cat9"
recordingpathcat10 = projectpath + "/recordings/cat10"
recordingpathcat11 = projectpath + "/recordings/gencat"
#.upload categories .mp3 file save path
uploadpath = "/var/www/html/.upload"
uploadpath1to9 = uploadpath + "/cat"
uploadpathcat1 = uploadpath + "/cat1"
uploadpathcat2 = uploadpath + "/cat2"
uploadpathcat3 = uploadpath + "/cat3"
uploadpathcat4 = uploadpath + "/cat4"
uploadpathcat5 = uploadpath + "/cat5"
uploadpathcat6 = uploadpath + "/cat6"
uploadpathcat7 = uploadpath + "/cat7"
uploadpathcat8 = uploadpath + "/cat8"
uploadpathcat9 = uploadpath + "/cat9"
uploadpathcat10 = uploadpath + "/cat10"
uploadpathcat11 = uploadpath + "/gencat"
#LED's config:
#------------
# led1 = LED(18) #GPIO18 - LED1
# led2 = LED(23) #GPIO23 - LED2
# #led3 = LED(24) #GPIO24 - LED3
# led4 = LED(25) #GPIO25 - LED4
# led5 = LED(8)  #GPIO8  - LED5
# led6 = LED(7)  #GPIO7  - LED6
# led7 = LED(12) #GPIO12 - LED7
# led8 = LED(16) #GPIO16 - LED8
# led9 = LED(20) #GPIO20 - LED9
# #led11 = LED(21) #GPIO21 - LED11
# led10 = LED(14) #GPIO14 - LED10

# led = None
# led = DualLED(21,24)

# #GPIO's config:
# #-------------
# but1 = Button(17) #17 - cat1
# but2 = Button(27) #27 - cat2
# but3 = Button(22) #22 - cat3
# but4 = Button(10) #10 - cat4
# but5 = Button(9)  #9  - cat5
# but6 = Button(11) #11 - cat6
# but7 = Button(5)  #5  - cat7
# but8 = Button(6)  #6  - cat8
# but9 = Button(13) #13 - cat9
# but10 = Button(19)#19 - cat10
# but11 = Button(26)#26 - cat11
import RPi.GPIO as GPIO
from gpiozero import LED, Button
import time
import os
import socket
import subprocess
import wave
import contextlib
from datetime import datetime
from subprocess import check_output
import shutil



local_server = "192.168.1.53"

def is_connected(network):
    try:
        #if ".com" in network:
        #    network = socket.gethostbyname(network)
        s = socket.create_connection((network, 80))
        return True
    except:
        return False

projectpath =  os.path.split(os.path.realpath(__file__))[0]
audioguidepath = projectpath + "/audio-alert"
#local categories .wav file save path
recordingpath1to9 = projectpath + "/recordings/cat1"

#os.system("mkdir /home/pi/Documents/Shiva/")

if is_connected(local_server):
    print("Local server detected")
    upfiles = os.listdir(recordingpath1to9)
    if not upfiles:
        print("No files present")
    else:
        for i in upfiles:
            print("count")
            os.system("sshpass -p 'raspberry' rsync "+recordingpath1to9+"/" " pi@"+local_server+":/home/pi/Documents/")
            #os.system("sshpass -p 'raspberry' rsync "+ " pi@"+local_server+":/home/pi/Documents/radiotune.mp3" recordingpath1to9+"/"+i+)
   # os.system("chromium-browser --app=http://"+local_server+" &") 
else:
    print("Local server not detected")    
    
    
    
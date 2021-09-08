#!/usr/bin/python
# @brief: Script to upload files to google drive and download files
#         automatically .upload folder.
#         This script will be invoked on boot.
#
# @ver: 1.0
#----------------------------------------------------------------#
# ##   # #### ##   ## ###  #  #  ##  ####   #### ###  ##### #### #
# # #  # #  # # # # # #  # #  # # #  #   #  #  # #  #   #   #  # #
# #  # # #**# #  #  # #  # #  #   #  ####   #### #  #   #   #  # #
# #   ## #  # #     # ###  ####  ### #    # #  # ###  ##### #### #
#----------------------------------------------------------------#
# *** Libraries *** #
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
from dualled import DualLED

# setting folder paths
projectpath =  os.path.split(os.path.realpath(__file__))[0]
audioguidepath = projectpath + "/audio-alert"
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
recordingpathgencat = projectpath + "/recordings/gencat"

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
uploadpathgencat = uploadpath + "/gencat"

''' *** Global variables *** '''
penDet = False
ret = None
found = False

#destination path - Do not change the path
destpath_gdrive = "/home/pi/mnt/gdrive/cat"
destpath_gdrivegencat = "/home/pi/mnt/gdrive/gencat"
gdrivepath_broadcast = "/home/pi/mnt/gdrive/Ready_To_Broadcast/cat"
gdrivepath_broadcastgencat = "/home/pi/mnt/gdrive/Ready_To_Broadcast/gencat"

# network verification variables
remote_server = "www.google.com"
local_server = "192.168.11."

''' *** Global Functions *** '''
'''
    To check if Pi is connected to internet or local server
'''
def is_connected(network):
    try:
        #if ".com" in network:
        #    network = socket.gethostbyname(network)
        s = socket.create_connection((network, 80))
        return True
    except:
        return False

        
''' 
    To check if wifi is local network
'''        
def is_onradio():
    try:
        test = "Namdu1Radio" in check_output("iwgetid", universal_newlines=True)
        #print(test)
        return test
    except:
        return False

'''
    Macro for playing audio instructions - to keep the code simple
'''
def aplay(filename):
    os.system("aplay -D plughw:CARD=0,DEV=0 "+audioguidepath+"/"+filename)

'''
    Function to get the name of the pendrive connected
'''    
def getDevName():
    '''The below code to identify the pendrive folder name - Start'''
    try:
        os.system('rm -rf /home/pi/Documents/Namdu1Radio/usbs/usbs.txt')
    except:
        print("file not found")    
    os.system('ls /media/pi > /home/pi/Documents/Namdu1Radio/usbs/usbs.txt')
    file1 = open("/home/pi/Documents/Namdu1Radio/usbs/usbs.txt", "r")
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        line = line.rstrip("\n")
        ret = line
        penDet = True
        #print("Pendrive name:",ret)
        return ret
 
 
'''
    copy files to gdrive
'''
def copy2Gdrive(path1,path2,filename):
    #Upload the file to respective category in google drive
    src_Path = 'rclone move'+" "+path1+"/"+filename+" "+path2+"/" 
    #dst_Path = destpath+"i"
    print(src_Path)
    #print(dst_Path)
    os.system(src_Path)
    print ("upload success !!!")
    time.sleep(0.1)

led = None
led = DualLED(18,23)

# *** Setting up GPIO of Pi *** #
GPIO.setmode(GPIO.BCM)

os.system("sudo chmod -R 777 "+uploadpath)

#Added delay to ensure the Gdrive mounted properly





#time.sleep(20.0)

print("Started fileupload python file")

while True:

  

 
        for Dwnserver in range(170,180):
        
            #Get the available localserver ip
            DwnserverIP = local_server+str(Dwnserver)
            
            #Check the local server is available
            if is_connected(DwnserverIP):
                print("Local server for downloading detected",DwnserverIP)

            #loop for directories
            for y in range(1, 12):
            
                if y == 11:
                    path = uploadpathgencat
                else:
                    #src and dst path
                    path = uploadpath1to9+str(y)
                
                dwnfiles = os.listdir(path)
            
                if not dwnfiles:
                    print("No files to Download in cat",y)
                    #aplay("NothingToUploadcat1.wav")
                    continue
                else:
                    for k in dwnfiles:
                        led.fwd_blink("fast")
                        os.system("sshpass -p 'raspberry' rsync " "pi@"+DwnserverIP+":"+path+"/"+k+"  " +path+"/")
                        led.off()
            else:
                print("Local server for downloading not detected",DwnserverIP)            

#Info: Local server range 50 to 250 is defined in the router

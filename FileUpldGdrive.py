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
from subprocess import check_output
import shutil
from dualled import DualLED

# setting folder paths
projectpath =  os.path.split(os.path.realpath(__file__))[0]
audioguidepath = projectpath + "/audio-alert"
#local categories .wav file save path
recordingpath1to9 = projectpath +"/html/.upload/cat"
recordingpathcat1 = projectpath +"/html/.upload/cat1"
recordingpathcat2 = projectpath +"/html/.upload/cat2"
recordingpathcat3 = projectpath +"/html/.upload/cat3"
recordingpathcat4 = projectpath +"/html/.upload/cat4"
recordingpathcat5 = projectpath +"/html/.upload/cat5"
recordingpathcat6 = projectpath +"/html/.upload/cat6"
recordingpathcat7 = projectpath +"/html/.upload/cat7"
recordingpathcat8 = projectpath +"/html/.upload/cat8"
recordingpathcat9 = projectpath +"/html/.upload/cat9"
recordingpathcat10 = projectpath +"/html/.upload/cat10"
recordingpathgencat = projectpath +"/html/.upload/gencat"

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
destpath_gdrive = "/home/pi/mnt/gdrive/Ready_To_Broadcast/cat"
destpath_gdrivegencat = "/home/pi/mnt/gdrive/Ready_To_Broadcast/gencat"
gdrivepath_broadcast = "/home/pi/mnt/gdrive/Ready_To_Broadcast/cat"
gdrivepath_broadcastgencat = "/home/pi/mnt/gdrive/Ready_To_Broadcast/gencat"

# network verification variables
remote_server = "www.google.com"
local_server = "192.168.1."

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
os.system("fusermount -uz ~/mnt/gdrive")        
os.system("python3 ~/Documents/Namdu1Radio/mountdrive.py")
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
    os.system('rm -rf /home/pi/Documents/Namdu1Radio/usbs/usbs.txt')
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
    if "recorded" in filename or "comment" in filename:
        src_Path = 'rclone copy'+" "+path1+"/"+filename+" "+path2+"/" 
        #dst_Path = destpath+"i"
        print(src_Path)
        #print(dst_Path)
        os.system(src_Path)
        print ("upload success !!!")
        time.sleep(0.1)
    else:
        print("this is not a local recording")    

led = None
led = DualLED(18,23)

# *** Setting up GPIO of Pi *** #
GPIO.setmode(GPIO.BCM)

os.system("sudo chmod -R 777 "+uploadpath)

#Added delay to ensure the Gdrive mounted properly
time.sleep(20.0)

print("Started fileupload python file")

while True:

    ''' 
        The following code for Uploading files to localserver or Gdrive or pendrive
    '''
    
    #get the pendrive name
    devname =  getDevName()
    
    if devname != None:
        #update the destination path  
        destpath_pdrive = r"/media/pi/"+devname+r"/cat"
        
        #update the pendrive cat's path useful for copying data from/to
        destpath_pdrivegencat = r"/media/pi/"+devname+r"/gencat"
        
        #mount pendrive
        rv1 = subprocess.call("grep -qs '/media/pi' /proc/mounts", shell=True)
        rv2 = subprocess.call("mount | grep /media/pi", shell=True)
        penDet = False
        
    #Loop for all the categories (Total 11 cat's) available
    for x in range(1, 12):
        #src path
        localpaths = recordingpath1to9+str(x)
        
        #dst path
        destpath = destpath_gdrive+str(x)
        
        if devname != None:#if pendrive is connected
            destpath_pend = destpath_pdrive+str(x)
        
        if x == 11:
            #src path
            localpaths = recordingpathgencat
            
            #dst path
            destpath = destpath_gdrivegencat
            
            #if pendrive is connected
            if devname != None:
            
                #Update the destination path as pendrive gencat
                destpath_pend = destpath_pdrivegencat
            
            #Get the list of files present in a source path
            upfiles = os.listdir(localpaths)
        else:
            #Get the list of files present in a source path
            upfiles = os.listdir(localpaths)        
        
        if not upfiles:

            print("No files to upload in cat",x)
            continue
        else:
            if is_connected(remote_server):
                
                #Loop for files in a directory
                for i in upfiles:
                
                    #get the list of files in destination folder
                    chkfiles = os.listdir(destpath)
                    
                    #check is there any files present in a destination folder
                    if not chkfiles:
                    
                        #start blinking the led as upload started
                        led.fwd_blink("fast")
                        
                        print("uploading to internet cat",x)

                        #copy the file from source to destination
                        copy2Gdrive(localpaths, destpath, i)
                        
                        #stop blinking the led as upload stopped
                        led.off()
                    else:
                        #get the list of files in destination folder
                        for j in chkfiles:
                        
                            #check if the file is already present in a destination folder, if present don't copy
                            if i == j:
                            
                                #set the flag as file is already present
                                found = True
                                print("File already exists:",i)
                                
                                #remove the file from the source path
                                os.system("rm "+localpaths+"/"+i)
                                
                                continue
                                
                        #check the file present flag is set or not        
                        if found == False:
                          
                            #start blinking the led as upload started
                            led.fwd_blink("fast")
                            
                            print("uploading to internet cat",x)
                            
                            #copy the file from source to destination
                            copy2Gdrive(localpaths, destpath, i)
                            
                            #stop blinking the led as upload stopped
                            led.off()

                        else:
                            #Clear the flag
                            found = False
    
            elif devname != None:
                
                #Loop for files in a directory
                for i in upfiles:
                    
                    #Get the source path with file to be copied
                    src0 = localpaths+"/"+i
                    
                    #Get the dest path
                    dst0 = destpath_pend
                    
                    #Get the list of files in a destination folder
                    chkfiles = os.listdir(dst0)
                    
                    #Check is there any files presenr in a destination folder
                    if not chkfiles:
                    
                        #Start blinking the led as upload started
                        led.fwd_blink("fast")
                        
                        print("uploading to pendrive cat",x)
                        
                        #Start copying the file from source to destination
                        shutil.copy(src0, dst0)
                        
                        #Remove the source file after successfull copy
                        os.system("rm "+src0)
                        
                        #Stop blinking the led as upload stopped
                        led.off()
                    else:
                        #Check is there any files presenr in a destination folder
                        for j in chkfiles:
                        
                            #Check if the file is already present in a destination folder, if present don't copy
                            if i == j:
                                
                                #Set the flag, file is already present
                                found = True
                                
                                print("File already exists in pendrive:",i)
                                
                                #Remove the source file
                                os.system("rm "+src0)
                                
                                continue
                        #Check the flag is set or not
                        if found == False:
                            
                            #Start blinking the led as upload started
                            led.fwd_blink("fast")
                            
                            print("uploading to pendrive cat",x)

                            #Start copying the file from source to destination
                            shutil.copy(src0, dst0)
                            
                            #Remove the file
                            os.system("rm "+src0)
                            
                            #Stop blinking led
                            led.off()

                        else:
                            #Clear the flag
                            found = False                        
                    print ("Files copied to pendrive successfully !!!")                                



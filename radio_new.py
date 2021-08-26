#but11!/usr/bin/python
# @brief: Script to record and upload the audio files
#         GPIO's are used for recording and uploading
#         LED's  used for indicating respective category
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
import logging,coloredlogs
import os
import socket
import subprocess
import wave
import contextlib
from datetime import datetime
from subprocess import check_output
import shutil
from dualled import DualLED
from new_function import *
import sys
from selenium import webdriver
sys.path.append("/home/pi/Namdu1Radio/")
from globle_var import *
from selenium.webdriver.chrome.options import Options
#import logs
option = Options()
option.add_argument("--autoplay-policy=no-user-gesture-required")
driver= webdriver.Chrome(chrome_options=option)




#logging.basicConfig(filename="/opt/logfilename.log", level=logging.INFO)

# *** Global Variables *** #

#coloredlogs.install()
#code for the rotry swich

from RPi_GPIO_Rotary import rotary

## Define Callback functions

rotater_value=0
def cwTurn():

    logger1.info("CW Turn")

def ccwTurn():
    logger1.info("CCW Turn")

def buttonPushed():
    logger1.info("Button Pushed")


def valueChanged(count):
    global rotater_value
    rotater_value = count%10
    print(count%10) ## Current Counter value





## Initialise (clk, dt, sw, ticks)
obj = rotary.Rotary(16,20,21,2)

 ## Register callbacks
obj.register(increment=cwTurn, decrement=ccwTurn)

## Register more callbacks
obj.register(pressed=buttonPushed, onchange=valueChanged) 

## Start monitoring the encoder
obj.start() 




# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')


#def wavFilesJoin(file1,file):
    #a, fs, enc = audiolab.wavread('file1')
    #b, fs, enc = audiolab.wavread('file2')
    #c = scipy.vstack((a,b))
    #audiolab.wavwrite(c, 'file3.wav', fs, enc)
    #return file3.wav



# *** Setting up GPIO of Pi *** #
GPIO.setmode(GPIO.BCM)
#time.sleep(10.0)
#led.fwd_on()
#Pi started indication audio
logger1.info("pi Started")
logger2.info("pi Started")
#Test folder to verify local backup play
aplay("lappiready.wav")
#time.sleep(3.0)

while True:
    logger1.info("pi Running")
    logger2.info("pi Running")
    #led.off()
    #led.fwd_on()
    #Check whether local server connected
 
    if is_onradio() and is_connected(local_server) and cntr:
        os.system("pkill -9 aplay")
        time.sleep(0.1)
        logger1.info ("starting namma school radio....from local server ")
        logger2.info ("starting namma school radio....from local server ")
        aplay("radiostart.wav")
        #time.sleep(3)
        aplay("radiostart.wav")
        driver.get("http://localhost")  
        chromium_playing=True
        #time.sleep(3)
      #  driver.execute_script('document.getElementsByTagName("audio")[0].play()')   
        cntr = False
        playpause = True
    # #Check whether the internet is available to play from the website
    elif cntr == True:
        logger1.info ("Local and remote server not available")
        logger2.info ("Local and remote server not available")
        logger1.info ("Audio starts from localhost")
        logger2.info ("Audio starts from localhost")
        os.system("pkill -9 aplay")
        src_renamPath = r'/var/www/html/indexgencat.php'
        dst_renamPath = r'/var/www/html/index.php'
        shutil.copy(src_renamPath, dst_renamPath)
        time.sleep(3)
        aplay("radiostart.wav")
        driver.get("http://localhost/new")
        chromium_playing=True
        time.sleep(3)
      #  driver.execute_script('document.getElementsByTagName("audio")[0].play()')
        cntr = False
        playpause = True
        time.sleep(0.2)
        
    
    ''' if button1 is pressed - Category 1 functionality button '''
    
    if rotater_value==1: 
        rotater_value="x"                                    #changeing for testing form but1.ispressed to true change back when done testing
        logger1.info("button1 pressed")
        main_fuction(logger1,"cat1",driver)
            
    ''' if button2 is pressed - Category 2 functionality button '''
    if rotater_value==2:
        rotater_value="x"
        logger1.info("button2 pressed")
        main_fuction(logger1,"cat2",driver)
    ''' if button3 is pressed - Category 3 functionality button '''
    if rotater_value==3:
        rotater_value="x"
        logger1.info("button3 pressed")
        main_fuction(logger1,"cat3",driver)
        
            #led3.off()
    ''' if button4 is pressed - Category 4 functionality button '''
    if rotater_value==4:
        rotater_value="x"
        logger1.info("button4 pressed")
        main_fuction(logger1,"cat4",driver)
    ''' if button5 is pressed - Category 5 functionality button '''
    if rotater_value==5:
        rotater_value="x"
        logger1.info("button5 pressed")
        main_fuction(logger1,"cat5",driver)
    ''' if button6 is pressed - Category 6 functionality button '''
    if rotater_value==6:
        rotater_value="x"
        logger1.info("button6 pressed")
        main_fuction(logger1,"cat6",driver)
    ''' if button7 is pressed - Category 7 functionality button '''
    if rotater_value==7:
        rotater_value="x"
        logger1.info("button7 pressed")
        main_fuction(logger1,"cat7",driver)
    ''' if button8 is pressed - Category 8 functionality button '''
    if rotater_value==8:
        rotater_value="x"
        logger1.info("button8 pressed")
        main_fuction(logger1,"cat8",driver)
    ''' if button9 is pressed - Category 9 functionality button '''
    if rotater_value==9:
        rotater_value="x"
        logger1.info("button9 pressed")
        main_fuction(logger1,"cat9",driver)
    if rotater_value==10:
        rotater_value="x"
        logger1.info("button10 pressed")
        main_fuction(logger1,"cat10",driver)
    if rotater_value==0:
        rotater_value="x"
        #os.system("killall chromium-browser")
        #os.system("pkill -o chromium")
        logger1.info("buttons 11 pressed")
        main_fuction(logger1,"gencat",driver)

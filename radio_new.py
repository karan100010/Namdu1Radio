444#but11!/usr/bin/python
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
option.add_argument("--headless")
option.add_argument("--autoplay-policy=no-user-gesture-required")
driver= webdriver.Chrome(chrome_options=option)
volume_mode=False
preview=False
disable_pauseplay=False
cw_turn=False
ccw_turn=False
playpause=False


mapping=["gencat","cat1","cat2","cat3","cat4","cat5","cat6","cat7","cat8","cat9","cat10"]


def main_fuction(logger,catname,driver):
        global chromium_playing
       
        #global button_press
        global longpress
        global playpause
        global btn
        gencatpreview=False
        try:
            driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
        except Exception as e:
            logging.error('e')
        
        #while button_press==1:
            
            #Check if the button is pressed for > 2sec
#             if time.time() - previousTime > 2.0:
                
     
        if gencatpreview == True:
            gencatpreview = False
            
            logger.info("Gen cat preview stopped")
            os.system("pkill -9 aplay")
        
            #break
        #Check whether the local server is connected    
        elif is_onradio() and is_connected(local_server):
            os.system("pkill -9 aplay")
            
            # os.system("killall chromium-browser")
            # os.system("pkill -o chromium")
           # driver.close()
           # driver=webdriver.Chrome(chrome_options=option)
            
            
            logger.info ("starting namma school radio....from local server ")
            time.sleep(0.4)
            aplay("radiostart.wav")
            time.sleep(0.4)
            #driver.get("http://localhost/new")
            driver.get("http://localhost/")
            chromium_playing=True
            #time.sleep(3)

            
            playpause = True
        # Check whether the internet is available to play from the website
        # elif is_connected(remote_server):
            # start_radio_from_internet()                      
            # playpause = True
        else:
            logger.info ("Button11 general playback started")
            # os.system("pkill -9 aplay")
            # os.system("pkill -o chromium")
            # driver.close()
            # driver=webdriver.Chrome(chrome_options=option)
            aplay("radiostart.wav")
            src_renamPath = r'/var/www/html/index'+catname+'.php'
            chromium_playing=True
            dst_renamPath = r'/var/www/html/index.php'
            shutil.copy(src_renamPath, dst_renamPath)
            #Starts playing mp3 from .upload folder
            logger.info("starting audio form localhost in gencat")
            driver.get("http://localhost/index"+catname+".php")
            
            #time.sleep(3)
            # driver.execute_script('document.getElementsByTagName("audio")[0].play()')
            


def record(driver,catname,logger):
    global longpress
    global playpause
    global btn
    global chromium_playing
    global preview
    global disable_pauseplay
    disable_pauseplay=True
    try:
        driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
       # chromium_playing=False
        
    except Exception as e:
        logging.error(e)
        chromium_playing=False
    gencatpreview=False
    logger.info(chromium_playing)
    if not chromium_playing:
                f = open("/var/www/html/MediaUpload/current_link.txt", "r")
                filepath=f.readline()
                name_prefix=filepath.split(".")[1].split("/")[-1]
                f.close()
                #led.fwd_blink("slow")
            #    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                
                #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)
                logger.info(" comment recording started")                
                time.sleep(2)
                
                time.sleep(2)
                recFileName = name_prefix+"_comment"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                logger.info(recFileName)
                
                # records with 48000 quality
                rec_start_time=time.time()
                
                if os.system("arecord "+recFileName+".wav" +" &")==0:
                    logger.info("audio getting recorded")
                else:
                    arecord(".",recFileName+".wav")   
                
                # scan for button press to stop recording
                preview=True
                btn.wait_for_press(90000)
                rec_end_time=time.time()
                os.system("pkill -9 arecord")
                os.system("pkill -9 aplay")
                aplay("Catgen_stop.wav")
                
                #time.sleep(1.4)
                logger.info(catname+" recording stopped")
                
                
                previewplay(".",recFileName+".wav")
                t=round(rec_end_time-rec_start_time)
                btn.wait_for_press(t)
                os.system("pkill -9 aplay")
                try:
                    driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                    chromium_playing=True
                    
                except Exception as e:
                    logging.error('e')
                
                logger.info(rec_start_time-rec_end_time)
               
                
                
                
                    
                #time.sleep(10)
                
                try:
                    os.system("sudo lame -b 320 "+recFileName+".wav " "/var/www/html/.upload/"+catname+"/"+recFileName+".mp3")
                except Exception as e:
                    logger.error(e)    
                os.system("rm "+recFileName+".wav")
                
                
                # os.system("lxterminal -e python "+projectpath+"/Wav2Mp3Convert.py  &")
                # shutil.copyfile(recordingpathcat11+"/"+recFileName+".mp3","/var/www/html/new/.upload/"+recFileName+"mp3")
                # os.system("rm "+recFileName)
                #led.fwd_on()
                longpress = False
                gencatpreview = True
                p=False
                chromium_playing=True
                disable_pauseplay=False
    else:           
                    disable_pauseplay=True
            
                    
                    
                    #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)

                    logger1.info("Gencat recording started")
                    
                    
                    # driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                    

                    
                    #time.sleep(1.0)
                    recFileName = "recorded@"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                    # records with 48000 quality
                    logger1.info(recFileName)
                    logger2.info(recFileName)
                    # records with 48000 quality
                    rec_start_time=time.time()
                    if os.system("arecord "+recFileName+".wav" +" &")==0:
                        logger1.info("audio getting recorded")
                        logger2.info("audio getting recorded")
                    else:
                        arecord(".",recFileName+".wav")    

                    # scan for button press to stop recording
                    btn.wait_for_press(90000)
                    os.system("pkill -9 arecord")
                    os.system("pkill -9 aplay")
                    aplay("Catgen_stop.wav")
                
                    #time.sleep(1.4)
                    logger.info(catname+" recording stopped")
                    rec_end_time=time.time()
                    
                    previewplay(".",recFileName+".wav")
                    t=round(rec_end_time-rec_start_time)
                    btn.wait_for_press(t)
                    os.system("pkill -9 aplay")
                    try:
                        driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                    except Exception as e:
                        logging.error('e')
                    
                    logger.info(rec_start_time-rec_end_time)
                   
                    
                    try:
                        os.system("sudo lame -b 320 "+recFileName+".wav " "/var/www/html/.upload/"+catname+"/"+recFileName+".mp3")
                    except Exception as e:
                        logger.error(e)    
                    os.system("rm "+recFileName+".wav")    
                        
                    
                    longpress = False
                    p=False


                    gencatpreview = True
                    disable_pauseplay=False
                
            






#logging.basicConfig(filename="/opt/logfilename.log", level=logging.INFO)

# *** Global Variables *** #

#coloredlogs.install()
#code for the rotry swich

from RPi_GPIO_Rotary import rotary

## Define Callback functions




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


rotater_value=0
def cwTurn():
    global cw_turn

    logger1.info("CW Turn")
    cw_turn= True

def ccwTurn():
    global ccw_turn
    logger1.info("CCW Turn")
    ccw_turn=True

def buttonPushed():
    logger1.info("Button Pushed")
    return True

    

def valueChanged(count):
    if not volume_mode:

        global rotater_value
        rotater_value = count%11
        print(count%11) ## Current Counter value





## Initialise (clk, dt, sw, ticks)
obj = rotary.Rotary(16,20,21,2)

 ## Register callbacks
obj.register(increment=cwTurn, decrement=ccwTurn)

## Register more callbacks
obj.register(pressed=buttonPushed, onchange=valueChanged) 

## Start monitoring the encoder
obj.start() 

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
  
       
        time.sleep(3)
      #  driver.execute_script('document.getElementsByTagName("audio")[0].play()')
        cntr = False
        playpause = True
        time.sleep(0.2)
        
    ''' if button1 is pressed - Category 1 functionality button '''
    if btn.is_pressed:
        disable_longpress=False
        if  disable_pauseplay==False:
            print("button pressed")
            previousTime = time.time()
            while btn.is_pressed:
                if cw_turn:
                   
                    os.system("amixer set Master 10%+")
                    logger1.info("audio increased by 10%")
                    volume_mode=True
                    cw_turn=False
                   
                if ccw_turn:
                    
                    
                    os.system("amixer set Master 10%-") 
                    logger1.info("audio decreased by 10%") 
                    ccw_turn=False
                    volume_mode=True
                #Check if the button is pressed for > 2sec
                   
                if time.time() - previousTime > 2.0:
                    if not volume_mode:
                            longpress=True
            
            if chromium_playing:
                try:
                    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                    chromium_playing=False
                    logging.info(chromium_playing)
                except Exception as e:
                    logger1.info(e)    
            else:
                try:
                    driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                    chromium_playing=True
                except Exception as e:
                    logger1.info(e)    
        logging.info(chromium_playing)            
        if longpress:
            try:
                    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
            except Exception as e:
                        logging.error(e)
            
            logging.info(chromium_playing)
            logger1.info('a longpress')
            aplay("beep_catgen.wav")
            record(driver,mapping[val],logger1)
            longpress=False
            
                   
                          
                          
                            #if the button is pressed for more than two seconds, ten longpress is Tr
    if not volume_mode:
        if rotater_value==1: 
            val=1                                    #changeing for testing form but1.ispressed to true change back when done testing
            logger1.info("button1 pressed")
            main_fuction(logger1,"cat1",driver)
            rotater_value="x"
                
        ''' if button2 is pressed - Category 2 functionality button '''
        if rotater_value==2:
            val=2
            rotater_value="x"
            logger1.info("button2 pressed")
            main_fuction(logger1,"cat2",driver)
        ''' if button3 is pressed - Category 3 functionality button '''
        if rotater_value==3:
            val=3
            rotater_value="x"
            logger1.info("button3 pressed")
            main_fuction(logger1,"cat3",driver)
            
                #led3.off()
        ''' if button4 is pressed - Category 4 functionality button '''
        if rotater_value==4:
            val=4
            rotater_value="x"
            logger1.info("button4 pressed")
            main_fuction(logger1,"cat4",driver)
        ''' if button5 is pressed - Category 5 functionality button '''
        if rotater_value==5:
            val=5
            rotater_value="x"
            logger1.info("button5 pressed")
            main_fuction(logger1,"cat5",driver)
        ''' if button6 is pressed - Category 6 functionality button '''
        if rotater_value==6:
            val=6
            rotater_value="x"
            logger1.info("button6 pressed")
            main_fuction(logger1,"cat6",driver)
        ''' if button7 is pressed - Category 7 functionality button '''
        if rotater_value==7:
            val=7
            rotater_value="x"
            logger1.info("button7 pressed")
            main_fuction(logger1,"cat7",driver)
        ''' if button8 is pressed - Category 8 functionality button '''
        if rotater_value==8:
            val=8
            rotater_value="x"
            logger1.info("button8 pressed")
            main_fuction(logger1,"cat8",driver)
        ''' if button9 is pressed - Category 9 functionality button '''
        if rotater_value==9:
            val=9
            rotater_value="x"
            logger1.info("button9 pressed")
            main_fuction(logger1,"cat9",driver)
        if rotater_value==10:
            val=10
            rotater_value="x"
            logger1.info("button10 pressed")
            main_fuction(logger1,"cat10",driver)
        if rotater_value==0:
            val=0
            #os.system("killall chromium-browser")
            #os.system("pkill -o chromium")
            logger1.info("buttons 11 pressed")
            main_fuction(logger1,"gencat",driver)
            rotater_value="x"
    volume_mode=False    


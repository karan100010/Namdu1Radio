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
coloredlogs.install()



#logging.basicConfig(filename="/opt/logfilename.log", level=logging.INFO)

# *** Global Variables *** #

coloredlogs.install()
import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/temp/myapp.log',
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


#def wavFilesJoin(file1,file):
    #a, fs, enc = audiolab.wavread('file1')
    #b, fs, enc = audiolab.wavread('file2')
    #c = scipy.vstack((a,b))
    #audiolab.wavwrite(c, 'file3.wav', fs, enc)
    #return file3.wav



# *** Setting up GPIO of Pi *** #
GPIO.setmode(GPIO.BCM)
#time.sleep(10.0)
led.fwd_on()
#Pi started indication audio
logging.info("pi Started")
#Test folder to verify local backup play
aplay("lappiready.wav")
#time.sleep(3.0)

while True:
    logging.info("pi Running")
    #led.off()
    #led.fwd_on()
    #Check whether local server connected
 
    if is_onradio() and is_connected(local_server) and cntr:
        os.system("pkill -9 aplay")
        time.sleep(0.1)
        logging.info ("starting namma school radio....from local server ")
        aplay("radiostart.wav")
        #time.sleep(3)
        aplay("radiostart.wav")
        driver.get("http://localhost/new")  
        chromium_playing=True
        #time.sleep(3)
      #  driver.execute_script('document.getElementsByTagName("audio")[0].play()')   
        cntr = False
        playpause = True
    # #Check whether the internet is available to play from the website
    elif cntr == True:
        logging.info ("Local and remote server not available")
        logging.info ("Audio starts from localhost")
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
    
    if but1.is_pressed:                                     #changeing for testing form but1.ispressed to true change back when done testing
        logging.info("button1 pressed")
        previousTime = time.time()
        time.sleep(0.2)
       
        while but1.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but2.is_pressed) or (but3.is_pressed) or (but4.is_pressed)or  
                (but5.is_pressed) or (but6.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                   # shutdownPi()
                   logging.info("hi")
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat1.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
    
        if longpress:
            record(but1,stop_audio["Cat1"],recordingpathcat1,uploadpathcat1,led1)           
            #os.system("rm "+recordingpathcat1+"/recorded_audio.wav") #remove the recorded file
            longpress = False
            cat1playpause = True
            cat1preview = True
            led1.off()
            
            #break
        else:
            cat1playpause=False
            playaudio("Cat1",led1,cat10preview)
            
    ''' if button2 is pressed - Category 2 functionality button '''
    if but2.is_pressed:
        logging.info("button2 pressed")
        previousTime = time.time()
        while but2.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but3.is_pressed) or (but4.is_pressed)or  
                (but5.is_pressed) or (but6.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat2.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        
        if longpress:
            record(but2,stop_audio["Cat2"],recordingpathcat2,uploadpathcat2,led2)
                   
            #os.system("rm "+recordingpathcat1+"/recorded_audio.wav") #remove the recorded file
            longpress = False
            cat2playpause = True
            cat2preview = True
            led2.off()
            
            #break
        else:
            led2.on()
            pfiles = os.listdir(uploadpathcat2)
            if cat2preview == True:
                cat2preview = False
                logging.info("Cat2 preview stopped")
                os.system("pkill -9 aplay")
            elif cat2playpause == True:

                cat2playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                                        
                playpause = True
                cat2playpause = True
            elif not pfiles:
                logging.info("No files to play in cat2")
                aplay("NofilesinCat2.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat2.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat2.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led2.off()
    ''' if button3 is pressed - Category 3 functionality button '''
    if but3.is_pressed:
        logging.info("button3 pressed")
        previousTime = time.time()
        while but3.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but4.is_pressed)or  
                (but5.is_pressed) or (but6.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat3.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            
            record(but3,stop_audio["Cat3"],recordingpathcat3,uploadpathcat3) 
            #led3.on()

            longpress = False
            cat3playpause = True
            cat3preview = True
        #led3.off()
            #break
        else:
            #led3.on()
            pfiles = os.listdir(uploadpathcat3)
            if cat3preview == True:
                cat3preview = False
                logging.info("Cat3 preview stopped")
                os.system("pkill -9 aplay")
            elif cat3playpause == True:
                stop_radio()
                cat3playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()                        
                playpause = True
                cat3playpause = True
            elif not pfiles:
                logging.info("No files to play in cat3")
                aplay("NofilesinCat3.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat3.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat3.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            #led3.off()
    ''' if button4 is pressed - Category 4 functionality button '''
    if but4.is_pressed:
        logging.info("button4 pressed")
        previousTime = time.time()
        while but4.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but5.is_pressed) or (but6.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat4.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but1,stop_audio["Cat4"],recordingpathcat4,uploadpathcat4,led4)
            longpress = False
            cat4playpause = True
            cat4preview = True
            led4.off()
            #break
        else:
            led4.on()
            pfiles = os.listdir(uploadpathcat4)
            if cat4preview == True:
                cat4preview = False
                logging.info("Cat4 preview stopped")
                os.system("pkill -9 aplay")
            elif cat4playpause == True:
                stop_radio()
                cat4playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat4playpause = True
            elif not pfiles:
                logging.info("No files to play in cat4")
                aplay("NofilesinCat4.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat4.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat4.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led4.off()
    ''' if button5 is pressed - Category 5 functionality button '''
    if but5.is_pressed:
        logging.info("button5 pressed")
        previousTime = time.time()
        while but5.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but6.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat5.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but5,stop_audio["Cat5"],recordingpathcat5,uploadpathcat5,led5)
            longpress = False
            cat5playpause = True
            cat5preview = True
            led5.off()
            #break
        else:
            led5.on()
            pfiles = os.listdir(uploadpathcat5)
            if cat5preview == True:
                cat5preview = False
                logging.info("Cat5 preview stopped")
                os.system("pkill -9 aplay")
            elif cat5playpause == True:
                stop_radio()
                cat5playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat5playpause = True
            elif not pfiles:
                logging.info("No files to play in cat5")
                aplay("NofilesinCat5.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat5.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat5.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led5.off()
    ''' if button6 is pressed - Category 6 functionality button '''
    if but6.is_pressed:
        logging.info("button6 pressed")
        previousTime = time.time()
        while but6.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but5.is_pressed) or (but7.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat6.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(led6,but6,stop_audio["Cat6"],recordingpathcat6,uploadpathcat6,led6)
            longpress = False
            cat6playpause = True
            cat6preview = True
            led6.off()
            #break
        else:
            led6.on()
            pfiles = os.listdir(uploadpathcat6)
            if cat6preview == True:
                cat6preview = False
                logging.info("Cat6 preview stopped")
                os.system("pkill -9 aplay")
            elif cat6playpause == True:
                stop_radio()
                cat6playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat6playpause = True
            elif not pfiles:
                logging.info("No files to play in cat6")
                aplay("NofilesinCat6.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat6.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat6.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led6.off()
    ''' if button7 is pressed - Category 7 functionality button '''
    if but7.is_pressed:
        logging.info("button7 pressed")
        previousTime = time.time()
        while but7.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but5.is_pressed) or (but6.is_pressed) or 
                (but8.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat7.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but7,stop_audio["Cat7"],recordingpathcat7,uploadpathcat7,led7)
            longpress = False
            cat7playpause = True
            cat7preview = True
            led7.off()
            #break
        else:
            led7.on()
            pfiles = os.listdir(uploadpathcat7)
            if cat7preview == True:
                cat7preview = False
                logging.info("Cat7 preview stopped")
                os.system("pkill -9 aplay")
            elif cat7playpause == True:
                stop_radio()
                cat7playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()

                playpause = True
                cat7playpause = True
            elif not pfiles:
                logging.info("No files to play in cat7")
                aplay("NofilesinCat7.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat7.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat7.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led7.off()
    ''' if button8 is pressed - Category 8 functionality button '''

    if but8.is_pressed:
        logging.info("button8 pressed")
        previousTime = time.time()
        while but8.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but5.is_pressed) or (but6.is_pressed) or 
                (but7.is_pressed) or (but9.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat8.wav")
                break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but8,stop_audio["Cat8"],recordingpathcat8,uploadpathcat8,led8)
            longpress = False
            cat8playpause = True
            cat8preview = True
            led8.off()
            #break
        else:
            led8.on()
            pfiles = os.listdir(uploadpathcat8)
            if cat8preview == True:
                cat8preview = False
                logging.info("Cat8 preview stopped")
                os.system("pkill -9 aplay")
            elif cat8playpause == True:
                stop_radio()
                cat8playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat8playpause = True
            elif not pfiles:
                logging.info("No files to play in cat8")
                aplay("NofilesinCat8.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat8.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat8.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led8.off()
    ''' if button9 is pressed - Category 9 functionality button '''
    if but9.is_pressed:
        logging.info("button9 pressed")
        previousTime = time.time()
        while but9.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but5.is_pressed) or (but6.is_pressed) or 
                (but7.is_pressed) or (but8.is_pressed) or (but10.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat9.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but9,stop_audio["Cat9"],recordingpathcat9,uploadpathcat9,led9)
            longpress = False
            cat9playpause = True
            cat9preview = True
            led9.off()
            #break
        else:
            led9.on()
            pfiles = os.listdir(uploadpathcat9)
            if cat9preview == True:
                cat9preview = False
                logging.info("Cat9 preview stopped")
                os.system("pkill -9 aplay")
            elif cat9playpause == True:
                stop_radio()
                cat9playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat9playpause = True
            elif not pfiles:
                logging.info("No files to play in cat9")
                aplay("NofilesinCat9.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat9.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat9.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led9.off()
    ''' if button10 is pressed - Category 10 functionality button '''
    if but10.is_pressed:
        logging.info("button10 pressed")
        previousTime = time.time()
        while but10.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                if((but1.is_pressed) or (but2.is_pressed) or (but3.is_pressed)or  
                (but4.is_pressed) or (but5.is_pressed) or (but6.is_pressed) or 
                (but7.is_pressed) or (but8.is_pressed) or (but9.is_pressed) or (but11.is_pressed)):
                    #if any of the buttons 2 to 9 is also pressed and held, then shutdown the Pi
                    shutdownPi()
                #if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                aplay("beep_cat10.wav")
                #break
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            record(but10,stop_audio["Cat10"],recordingpathcat10,uploadpathcat10,led10)
            longpress = False
            cat10playpause = True
            cat10preview = True
            led10.off()
            #break
        else:
            led10.on()
            pfiles = os.listdir(uploadpathcat10)
            if cat10preview == True:
                cat10preview = False
                logging.info("Cat10 preview stopped")
                os.system("pkill -9 aplay")
            elif cat10playpause == True:
                stop_radio()
                cat10playpause = False
                playpause = False
            elif is_connected(remote_server):
                start_radio_from_internet()
                playpause = True
                cat10playpause = True
            elif not pfiles:
                logging.info("No files to play in cat10")
                aplay("NofilesinCat10.wav")
            else:
                os.system("pkill -9 aplay")
                time.sleep(0.4)
                aplay("Cat10.wav")
                time.sleep(0.4)
                os.system("killall chromium-browser")
                os.system("pkill -o chromium")
                src_renamPath = r'/var/www/html/indexcat10.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                os.system("chromium-browser localhost &")
                time.sleep(0.2)
                playpause = True               
            led10.off()   
    '''upload and backup play functionality'''
    p=True
    if but11.is_pressed:
        #os.system("killall chromium-browser")
        #os.system("pkill -o chromium")
        logging.info("buttons 11 pressed")
        previousTime = time.time()
        
        
        while but11.is_pressed:
            #Check if the button is pressed for > 2sec
            if time.time() - previousTime > 2.0:
                
                if chromium_playing:
                    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                aplay("beep_catgen.wav")
              
                if but1.is_pressed or but2.is_pressed or but3.is_pressed \
                or but4.is_pressed or but5.is_pressed or but6.is_pressed \
                or but7.is_pressed or but8.is_pressed or but9.is_pressed \
                or but10.is_pressed :
                    #if any of the buttons 1 to 9 is also pressed and held, then shutdown the Pi
                   #shutdownPi()
                   logging.info("hi")
                # if the button is pressed for more than two seconds, then longpress is True
                longpress = True
                break
                #aplay("beep_catgen.wav")
         

   # if longpress is True, record audio after a 'beep'
        if time.time() - previousTime < 0.1: continue
        time.sleep(0.5)
        if longpress:
            
            if chromium_playing:
                f = open("/var/www/html/new/MediaUpload/current_link.txt", "r")
                filepath=f.readline()
                name_prefix=filepath.split(".")[1].split("/")[-1]
                f.close()
                led.fwd_blink("slow")
            #    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                chromium_playing=False
                #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)
                logging.info("Gencat comment recording started")
                
                time.sleep(2)
               # aplay("beep_catgen.wav")
                time.sleep(2)
                recFileName = name_prefix+"_comment"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                logging.info(recFileName)
                # records with 48000 quality

                if os.system("arecord "+recFileName+".wav" +" &")==0:
                    logging.info("audio getting recorded")
                else:
                    arecord(".",recFileName+".wav")    
                # scan for button press to stop recording
                but11.wait_for_press(300)
                os.system("pkill -9 arecord")
                os.system("pkill -9 aplay")
                aplay("Catgen_stop.wav")
                
                #time.sleep(1.4)
                logging.info("Gencat recording stopped")
                
                # previewplay(".",recFileName+".wav")
                #time.sleep(10)
                
                driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                os.system("lame -b 320 "+recFileName+".wav " "/var/www/html/new/.upload/gencat/"+recFileName+".mp3")
                os.system("rm "+recFileName)
                
                
                # os.system("lxterminal -e python "+projectpath+"/Wav2Mp3Convert.py  &")
                # shutil.copyfile(recordingpathcat11+"/"+recFileName+".mp3","/var/www/html/new/.upload/"+recFileName+"mp3")
                # os.system("rm "+recFileName)
                led.fwd_on()
                longpress = False
                gencatpreview = True
                p=False
                chromium_playing=True
               

                 
                 

            else:    
                led.fwd_blink("slow")
                
                
                #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)

                logging.info("Gencat recording started")
                
                # driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                # chromium_playing=False

              #  aplay("beep_catgen.wav")
                #time.sleep(1.0)
                recFileName = "recorded@"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                # records with 48000 quality
                logging.info(recFileName)
                # records with 48000 quality
                if os.system("arecord "+recFileName+".wav" +" &")==0:
                    logging.info("audio getting recorded")
                else:
                    arecord(".",recFileName+".wav")    

                # scan for button press to stop recording
                but11.wait_for_press(30000)
                os.system("pkill -9 arecord")
                os.system("pkill -9 aplay")
                aplay("Catgen_stop.wav")
                time.sleep(5)
                
                #time.sleep(1.4)
                logging.info("Gencat recording stopped")
                #time.sleep(5.0)
                #previewplay(".",recFileName+".wav")
                time.sleep(5)
                # driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                os.system("lame -b 320 "+recFileName+".wav " "/var/www/html/new/.upload/gencat/"+recFileName+".mp3")
                os.system("rm "+recFileName)

                
                led.fwd_on()
                longpress = False
                p=False


                gencatpreview = True
                
            
        
           
        else:

            if gencatpreview == True:
                gencatpreview = False
                
                logging.info("Gen cat preview stopped")
                os.system("pkill -9 aplay")
            elif playpause == True:
                playpause = False
                logging.info ("echo closing radio !!!")
                # os.system("killall chromium-browser")
                # os.system("pkill -o chromium")
                #driver=webdriver.Chrome(chrome_options=option)
                driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                chromium_playing=False
                os.system("pkill -9 aplay")
                time.sleep(0.2)
                aplay("radiostop.wav")
                #break
            #Check whether the local server is connected    
            elif is_onradio() and is_connected(local_server):
                os.system("pkill -9 aplay")
                
                # os.system("killall chromium-browser")
                # os.system("pkill -o chromium")
               # driver.close()
               # driver=webdriver.Chrome(chrome_options=option)
                
                
                logging.info ("starting namma school radio....from local server ")
                time.sleep(0.4)
                aplay("radiostart.wav")
                time.sleep(0.4)
                #driver.get("http://localhost/new")
                driver.get("http://localhost/new")
                chromium_playing=True
                #time.sleep(3)

                
                playpause = True
            # Check whether the internet is available to play from the website
            # elif is_connected(remote_server):
                # start_radio_from_internet()                      
                # playpause = True
            else:
                logging.info ("Button11 general playback started")
                # os.system("pkill -9 aplay")
                # os.system("pkill -o chromium")
                # driver.close()
                # driver=webdriver.Chrome(chrome_options=option)
                aplay("radiostart.wav")
                src_renamPath = r'/var/www/html/indexgencat.php'
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                #Starts playing mp3 from .upload folder
                logging.info("starting audio form localhost in gencat")
                driver.get("http://localhost/new")
                chromium_playing=True
                time.sleep(3)
                # driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                
                time.sleep(0.2)
                playpause = True
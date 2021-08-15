import time
import os,sys
import socket
import subprocess
import wave
import contextlib
from datetime import datetime
from subprocess import check_output
import shutil
import logging
from globle_var import *



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

''' To check if wifi is local network '''        
def is_onradio():
    try:
        test = "Namdu1Radio" in check_output("iwgetid", universal_newlines=True)
        return test
    except:
        return False

'''
    Macro for playing audio instructions - to keep the code simple
'''
def aplay(filename):
    os.system("aplay "+audioguidepath+"/"+filename)
    
'''
    Macro for playing recorded audio
'''
def previewplay(path, filename):
    os.system("aplay "+path+"/"+filename+ "&")
    
    '''
    Macro for recording audio
'''
def arecord(path, filename):
    os.system("arecord "+path+"/"+filename+" -D sysdefault:CARD=1 -f dat &")
    
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

'''
    Function to shutdown pi
'''    
def shutdownPi():
    os.system("pkill -9 aplay")
    aplay("shutdown.wav")
    os.system("sleep 3s; shutdown now ")                                
    exit(0)

'''
    Function to join wavefiles
'''    


def copy2Gdir_to_drvie(path1,path2,filename,recording_path):
    #Upload the file to respective category in google drive
    src_Path = 'rclone move'+" "+path1+"/"+filename+" "+path2+"/" 
    #dst_Path = destpath+"i"
    print(src_Path)
    #print(dst_Path)
    os.system(src_Path)
    print ("upload success !!!")
    time.sleep(0.1)


def record(button,stopaudio,recording_path,uploadpath,led=None):
            if led:
                led.on()
            print("recording has started")
            os.system("kill ll chromium-browser")
            os.system("pkill -o chromium")
            #time.sleep(0.4)
            #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)
            #aplay("beep_cat1.wav")
            time.sleep(1.0)
            # records with 48000 quality
            arecord(previewaudioguidepath,"recorded_audio.wav") 
            # scan for button press to stop recording
           
            button.wait_for_press(timeout=10) # to be discussed
            os.system("pkill -9 arecord")
            os.system("pkill -9 aplay")
            time.sleep(0.4)
            aplay(stopaudio)
            print("recording stopped")
            time.sleep(5.0)
            previewplay(previewaudioguidepath,"recorded_audio.wav")
            recFileName = "recorded@"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
            # converting recorded audio to mp3 and rename with date and time of recording
            os.system("lame -b 320 "+previewaudioguidepath+"/recorded_audio.wav " +recording_path+"/"+recFileName+".mp3")
            #save the recorded audio in .upload folder respective category
            os.system("sudo cp "+recording_path+"/"+recFileName+".mp3 " +uploadpath+"/"+recFileName+".mp3 &")
            os.system("pkill -9 aplay")            
            #os.system("rm "+recording_path+"/recorded_audio.wav") #remove the recorded file 
    
def stop_radio():    
    os.system("killall chromium-browser")
    os.system("pkill -o chromium")
    os.system("pkill -9 aplay")
    logging.info("closing the radio button")
    
    time.sleep(0.4)
    aplay("radiostop.wav")       


def main_fuction(logger,catname,driver):
        global chromium_playing
       
        #global button_press
        global longpress
        global playpause
        global btn
        gencatpreview=False
        #while button_press==1:
            
            #Check if the button is pressed for > 2sec
#             if time.time() - previousTime > 2.0:
                
                
        if chromium_playing:
            try:
                driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                aplay("beep_catgen.wav")
            except Exception as e:
                logger.info("no audios to play")
                logger.error(e)
                    
              
#                 # if the button is pressed for more than two seconds, then longpress is True
                 #longpress = True
#                 break
#                 #aplay("beep_catgen.wav")
         

#    # if longpress is True, record audio after a 'beep'
#         if time.time() - previousTime < 0.1: 
#             continue
#         time.sleep(0.5)
        if btn.is_pressed:
            
            if chromium_playing:
                f = open("/var/www/html/new/MediaUpload/current_link.txt", "r")
                filepath=f.readline()
                name_prefix=filepath.split(".")[1].split("/")[-1]
                f.close()
                #led.fwd_blink("slow")
            #    driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                chromium_playing=False
                #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)
                logger.info(" comment recording started")
                
                time.sleep(2)
               # aplay("beep_catgen.wav")
                time.sleep(2)
                recFileName = name_prefix+"_comment"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                logger.info(recFileName)
                # records with 48000 quality

                if os.system("arecord "+recFileName+".wav" +" &")==0:
                    logger.info("audio getting recorded")
                else:
                    arecord(".",recFileName+".wav")    
                # scan for button press to stop recording
                btn.wait_for_press(300)
                os.system("pkill -9 arecord")
                os.system("pkill -9 aplay")
                aplay("Catgen_stop.wav")
                
                #time.sleep(1.4)
                logger.info(catname+" recording stopped")
                
                # previewplay(".",recFileName+".wav")
                #time.sleep(10)
                
                driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                os.system("lame -b 320 "+recFileName+".wav " "/var/www/html/new/.upload/"+catname+"/"+recFileName+".mp3")
                os.system("rm "+recFileName)
                
                
                # os.system("lxterminal -e python "+projectpath+"/Wav2Mp3Convert.py  &")
                # shutil.copyfile(recordingpathcat11+"/"+recFileName+".mp3","/var/www/html/new/.upload/"+recFileName+"mp3")
                # os.system("rm "+recFileName)
                #led.fwd_on()
                longpress = False
                gencatpreview = True
                p=False
                chromium_playing=True
               

                 
                 

            else:    
                #led.fwd_blink("slow")
                
                
                #os.system("pkill -9 aplay") # to stop playing recorded audio (if it was)

                logger.info(catname+" recording started")
                
                # driver.execute_script('document.getElementsByTagName("audio")[0].pause()')
                # chromium_playing=False

              #  aplay("beep_catgen.wav")
                #time.sleep(1.0)
                recFileName = "recorded@"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                # records with 48000 quality
                logger.info(recFileName)
                # records with 48000 quality
                if os.system("arecord "+recFileName+".wav" +" &")==0:
                    logger.info("audio getting recorded")
                else:
                    arecord(".",recFileName+".wav")    

                # scan for button press to stop recording
                btn.wait_for_press(30000)
                os.system("pkill -9 arecord")
                os.system("pkill -9 aplay")
                aplay("Catgen_stop.wav")
                time.sleep(5)
                
                #time.sleep(1.4)
                logger.info(catname+" recording stopped")
                #time.sleep(5.0)
                #previewplay(".",recFileName+".wav")
                time.sleep(5)
                # driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                os.system("lame -b 320 "+recFileName+".wav " "/var/www/html/new/.upload/"+catname+"/"+recFileName+".mp3")
                os.system("rm "+recFileName)

                
                #led.fwd_on()
                longpress = False
                p=False


                gencatpreview = True
                
            
        
           
        else:

            if gencatpreview == True:
                gencatpreview = False
                
                logger.info("Gen cat preview stopped")
                os.system("pkill -9 aplay")
            elif playpause == True:
                playpause = False
                logger.info ("echo closing radio !!!")
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
                dst_renamPath = r'/var/www/html/index.php'
                shutil.copy(src_renamPath, dst_renamPath)
                #Starts playing mp3 from .upload folder
                logger.info("starting audio form localhost in gencat")
                driver.get("http://localhost/")
                chromium_playing=True
                time.sleep(3)
                # driver.execute_script('document.getElementsByTagName("audio")[0].play()')
                
                time.sleep(0.2)
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
import os
from datetime import datetime
import fnmatch
import shutil
# setting folder paths
projectpath =  os.path.split(os.path.realpath(__file__))[0]
audioguidepath = projectpath + "/audio-alert"
previewaudioguidepath = projectpath + "/recordings/gencat"


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
uploadpath = "/var/www/html/new/.upload"
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

led = None

print("Monitoring for .wav to .mp3 file conversion")
while True:
    # Get list of files in a directory
    for x in range(1, 12):
        #src path
        srcpath = recordingpath1to9+str(x)
        #dst path
        dstpath = uploadpath1to9+str(x)
        if x == 11:
            #src path
            srcpath = recordingpathcat11
            #dst path
            dstpath = uploadpathcat11
        #Get the list of files in a directory
        files = os.listdir(srcpath)
        #Loop for files to be converted to mp3
        if not files:
            if x==11:
                print("No .wav file present in gencat")
            else:
                print("No .wav file present in cat",x)
        else:
            for i in files:
                if fnmatch.fnmatch(i, '*.wav'):
                    #print(i)
                    #Recorded file name
                    recFileName = "recorded@"+datetime.now().strftime('%d%b%Y_%H_%M_%S')
                    #start converting from .wav to mp3
                    os.system("lame -b 320 "+srcpath+"/"+i+" " +srcpath+"/"+i+".mp3")
                    #copy converted .mp3 to .upload folders
                    shutil(srcpath+"/"+i+".mp3",dstpath+"/"+i+".mp3")
                    #remove the .wav file
                    os.system("rm  "+recordingpathcat11+"/"+i+".wav")
                    
                else:
                    print("No .wav fies present for conversion")

    break


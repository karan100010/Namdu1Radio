import os
import socket
from subprocess import check_output
from time import sleep
from pathlib import Path
from typing import Tuple

''' *** Global Functions *** '''
'''
    To check if Pi is connected to internet or local server
'''
source_prefix="/var/www/html/.upload/"
remote_prefix="/home/pi/mnt/gdrive/Ready_To_Broadcast/"

def is_connected(network):
    try:
        #if ".com" in network:
        #    network = socket.gethostbyname(network)
        s = socket.create_connection((network, 80))
        return True
    except:
        return False

mapping=["gencat","cat1","cat2","cat3","cat4","cat5","cat6","cat7","cat8","cat9","cat10"]
def download_file(catlist):
    global source_prefix
    global remote_prefix
    for i in catlist:
        try:
            os.system("rsync -azPu "+remote_prefix+i+"/ "+source_prefix+i +"/ --ignore-existing")
        except:
            print("error occured while tranfering from "+i)


gdrive_path=Path('/home/pi/mnt/gdrive/Ready_To_Broadcast')

       
#os.system("fusermount -uz ~/mnt/gdrive")
if not gdrive_path.is_dir():
         
    os.system("python3 /home/pi/Documents/Namdu1Radio/mountdrive.py")
    sleep(30)
else:
    print("gdrive already mounted")    

while True:
    if gdrive_path.is_dir():
        
        download_file(mapping)
        os.system('python3 /home/pi/Documents/Namdu1Radio/FileUpldGdrive.py')
        break

    else:
        sleep(10)
        print("sleeping for 10 seconds")    

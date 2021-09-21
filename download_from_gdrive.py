import os
import socket
from subprocess import check_output
from time import sleep

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


def download_file(catlist):
    global source_prefix
    for i in catlist:
        try:
            os.system("rsync -azP "+remote_prefix+i+"/ "+source_prefix+i)
        except:
            print("error occured while tranfering from "+i)    
        
         




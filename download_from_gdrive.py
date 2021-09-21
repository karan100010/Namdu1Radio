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

mapping=["gencat","cat1","cat2","cat3","cat4","cat5","cat6","cat7","cat8","cat9","cat10"]
def download_file(catlist):
    global source_prefix
    for i in catlist:
        try:
            os.system("rsync -azP "+remote_prefix+i+"/ "+source_prefix+i +" --ignore-existing")
        except:
            print("error occured while tranfering from "+i)    
        os.system("sudo chmod -R 777 /var/www/html/.upload/")
os.system("fusermount -uz ~/mnt/gdrive")         
os.system("python3 ~/Documents/Namdu1Radio/mountdrive.py")
sleep(10)        

if is_connected("www.google.com"):
    
    download_file(mapping)

else:
    sleep(10)
    print("sleeping for 10")    


         




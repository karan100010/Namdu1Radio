import time
import os
import socket
from subprocess import check_output
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


       

               

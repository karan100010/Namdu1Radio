#!/usr/bin/python
# @brief: Script to mount google drive automatically
#         This script will be invoked on every boot
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
import socket
from subprocess import check_output
from time import sleep

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
    
#Mount the google to local folder
cntr = True
# network verification variables
remote_server = "www.google.com"
while True:
    if is_connected(remote_server):
        if cntr == True:
            os.system('rclone mount gdrive: $HOME/mnt/gdrive &')
            print("gdrive mounted")
            cntr = False
    else:
        sleep(30)
        print("No internet!!! Cannot mount Gdrive")
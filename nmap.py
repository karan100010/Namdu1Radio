import nmap
from subprocess import Popen
from time import sleep

def get_lan_ip():
    nm=nmap.PortScanner()
    nm.scan('192.168.1.1/24','22')
    return nm.all_hosts()
ip_list=["192.168.1.41","192.168.1.42","192.168.1.43","192.168.1.44","192.168.1.45"]
with open('ip_list.txt', 'w') as f:
    for item in ip_list:
        f.write("%s\n" % item)
while True:
    ip_list=get_lan_ip()
    with open('ip_list.txt', 'w') as f:
        for item in ip_list:
            f.write("%s\n" % item)
    sleep(300)

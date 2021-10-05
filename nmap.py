
from time import sleep
import nmap3

def get_lan_ip():
       
        nmap = nmap3.Nmap()
        results = nmap.scan_top_ports("192.168.1.1/24", args="-sn")
        return [i for i in results.keys() if "192.168" in i]
        
ip_list=["192.168.1.41","192.168.1.42","192.168.1.43","192.168.1.44","192.168.1.45"]
with open('ip_list.txt', 'w') as f:
    for item in ip_list:
        f.write("%s\n" % item)

ip_list=get_lan_ip()
with open('ip_list.txt', 'w') as f:
    for item in ip_list:
        f.write("%s\n" % item)


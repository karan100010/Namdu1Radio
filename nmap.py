
from time import sleep
import nmap3
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
ip=get_ip()    

def get_lan_ip():
       
        nmap = nmap3.Nmap()
        results = nmap.scan_top_ports(ip+"/24", args="-sn")
        return [i for i in results.keys() if "192.168" in i]

ip_list=get_lan_ip()
with open('ip_list.txt', 'w') as f:
    for item in ip_list:
        f.write("%s\n" % item)


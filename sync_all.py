from local_sync import *
from radio_new import logger1

with open("ip_list.txt") as file:
                    lines = file.readlines()
                    ipmap = [line.rstrip() for line in lines]
mapping=["gencat","cat1","cat2","cat3","cat4","cat5","cat6","cat7","cat8","cat9","cat10"]

for j in mapping:
    sync(j,ipmap,logger=logger1)
        
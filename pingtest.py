import speedtest,os,time


sp=speedtest.Speedtest()


while True:
    speed=speedtest.download()/20
    if speed>100:
        os.system("mountdrive.py")
        time.sleep(20)
        os.system("download_from_gdrive.py")
    else:
        time.sleep(5)    

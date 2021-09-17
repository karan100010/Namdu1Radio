
from subprocess import Popen
from multiprocessing import Process

    
def sync(catname,ipmap,logger):
    for i in ipmap:
        try:
            Popen("sshpass -f 'sshpass' rsync -azP /var/www/html/.upload/"+catname+" pi@"+i+":/var/www/html/.upload/"+catname+" --ignore-existing")
        except Exception as e:
            logger("following exception occred "+e+" while tranferring to "+i) 

        try:
            Popen("sshpass -f 'sshpass' rsync -azP pi@"+i+":/var/www/html/.upload/"+catname+"/ /var/www/html/.upload/"+catname+" --ignore-existing")
        except Exception as e:
            logger("following exception occred "+e+" while tranferring to "+i)     


def sync_background(catname,ipmap,logger):

    p = Process(target=sync, args=(catname,ipmap,logger,))
            # you have to set daemon true to not have to wait for the process to join
    p.daemon = True
    p.start()
    logger.info("syncing running in the background")


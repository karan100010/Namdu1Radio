from gpiozero import LED
from time import sleep

class DualLED(object):
    def __init__(self,pin1, pin2):
        
        self.pin1  = LED(pin1)
        self.pin2  = LED(pin2)
        self.off()
        self.slow = 0.5
        self.fast = 0.1

    def off(self):
        self.pin1.off()
        self.pin2.off()
        
    def fwd_on(self):
        self.pin1.on()
        self.pin2.off()
    
    def rev_on(self):
        self.pin1.off()
        self.pin2.on()
        
    def fwd_blink(self,speed):
        self.pin2.off()
        if "slow" in speed:
            self.pin1.blink(self.slow,self.slow)
        else:
            self.pin1.blink(self.fast,self.fast)
            
    def rev_blink(self,speed):
        self.pin1.off()
        if "slow" in speed:
            self.pin2.blink(self.slow,self.slow)
        else:
            self.pin2.blink(self.fast,self.fast)
        
    def blink(self,speed):
        self.pin2.off()
        if "slow" in speed:
            self.pin1.blink(self.slow,self.slow)
            sleep(self.slow)
            self.pin2.blink(self.slow,self.slow)
        else:
            self.pin1.blink(self.fast,self.fast)
            sleep(self.fast)
            self.pin2.blink(self.fast,self.fast)
            
if __name__ == "__main__":
    test = DualLED(21,24)
    while True:
        test.fwd_on()
    
        sleep(3)
        test.off()
        sleep(3)
        #test.rev_on()
        sleep(3)
        #test.off()
        sleep(3)
        test.fwd_blink("slow")
        sleep(10)
        test.rev_blink("fast")
        sleep(10)
        test.blink("fast")
        sleep(10)
        test.blink("slow")
        sleep(10)
        test.off()
    
            
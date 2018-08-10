import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

def destroy():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.setup(11, GPIO.IN)
    GPIO.setup(13, GPIO.IN)

def openLed():
    setup()
    GPIO.output(13, GPIO.HIGH)
    for i in range(2):
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11, GPIO.LOW)
        time.sleep(1)
#    destroy()
    GPIO.cleanup()

if __name__=="__main__":
    openLed()  

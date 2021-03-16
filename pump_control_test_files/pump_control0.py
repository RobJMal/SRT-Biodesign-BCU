# Tests the Pi's interface with the pump
import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

forward_pin = 33
backward_pin = 35
sleeptime = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)


def forward(x):
    GPIO.output(forward_pin, GPIO.HIGH)
    print("Moving forward")
    time.sleep(x)
    GPIO.output(forward_pin, GPIO.LOW)
    
def reverse(x):
    GPIO.output(backward_pin, GPIO.HIGH)
    print("Moving backward")
    time.sleep(x)
    GPIO.output(backward_pin, GPIO.LOW)
    
while (1):
    forward(2)
    reverse(2)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(forward_pin, GPIO.OUT)
    GPIO.setup(backward_pin, GPIO.OUT)

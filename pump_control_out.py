# Runs pump clockwise (pumping out) using TB6612FNG Motor Driver 
# https://howchoo.com/g/mjg5ytzmnjh/controlling-dc-motors-using-your-raspberry-pi 

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA (Orange)
GPIO.setup(11, GPIO.OUT) # Connected to AIN2 (Green)
GPIO.setup(12, GPIO.OUT) # Connected to AIN1 (Yellow)
GPIO.setup(13, GPIO.OUT) # Connected to STBY (Gray)

# Time that the motor is running 
time_run_out = 5

# Drive the motor clockwise (pumps water out)
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.HIGH) # Set AIN2

# Set the motor speed
GPIO.output(7, GPIO.HIGH) # Set PWMA

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
print("Running pump for " + str(time_run_out) + " seconds")
time.sleep(time_run_out)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY

# File: traffic_light_system.py
# Raspberry Pi Traffic Light Project

import RPi.GPIO as GPIO
import time

RED = 17
YELLOW = 27
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

try:
    while True:
        # RED ON
        GPIO.output(RED, 1)
        GPIO.output(YELLOW, 0)
        GPIO.output(GREEN, 0)
        print("STOP")
        time.sleep(5)

        # YELLOW ON
        GPIO.output(RED, 0)
        GPIO.output(YELLOW, 1)
        GPIO.output(GREEN, 0)
        print("WAIT")
        time.sleep(2)

        # GREEN ON
        GPIO.output(RED, 0)
        GPIO.output(YELLOW, 0)
        GPIO.output(GREEN, 1)
        print("GO")
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()

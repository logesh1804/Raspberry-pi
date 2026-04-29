# File: led_blink_rpi.py
# Raspberry Pi GPIO LED Blink

import RPi.GPIO as GPIO
import time

LED = 18   # GPIO18 (Pin 12)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)

        GPIO.output(LED, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

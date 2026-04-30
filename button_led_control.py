# File: today_commit_rpi_button_led.py
# Raspberry Pi LED Control using Push Button

import RPi.GPIO as GPIO
import time

LED = 18        # GPIO18 -> LED
BUTTON = 23     # GPIO23 -> Push Button

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(BUTTON)

        if button_state == 0:   # Button Pressed
            GPIO.output(LED, GPIO.HIGH)
            print("Button Pressed - LED ON")
        else:
            GPIO.output(LED, GPIO.LOW)
            print("Button Released - LED OFF")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

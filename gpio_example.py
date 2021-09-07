import RPi.GPIO as GPIO
import time
from datetime import datetime

# Determine the pin numbering schemes: GPIO.BOARD or GPIO.BCM
GPIO.setmode(GPIO.BOARD)

# Define the pin of the hardware
PIN_LED1 = 10
PIN_LED2 = 12
PIN_BUTTON = 11

# Setup pin mode
GPIO.setup(PIN_LED1, GPIO.OUT)
GPIO.setup(PIN_LED2, GPIO.OUT)
GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Wait until the button is pressed. Then, start blinking the LEDs alternately.
while(1):
    time.sleep(0.1)
    isButtonReleased = GPIO.input(PIN_BUTTON)

    if not(isButtonReleased):
        print("The button is pressed. Start flashing LED! ")
        # Blink LED alternately
        for i in range(5):
            print('Turning on LED1 ...')
            GPIO.output(PIN_LED1, GPIO.HIGH)
            time.sleep(0.25)

            print('Turning off LED1 ...')
            GPIO.output(PIN_LED1, GPIO.LOW)
            time.sleep(0.25)

            print('Turning on LED2 ...')
            GPIO.output(PIN_LED2, GPIO.HIGH)
            time.sleep(0.25)

            print('Turning off LED2 ...')
            GPIO.output(PIN_LED2, GPIO.LOW)
            time.sleep(0.25) 
        break
    else: 
        print("Waiting for the button to be pressed ...")   

# Clean up
print('Cleaning up GPIO ...')
GPIO.cleanup()
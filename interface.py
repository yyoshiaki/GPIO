from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

import RPi.GPIO as GPIO 
import time


#### config ####
gpio_led = 22
gpio_sw_1 = 26
gpio_sw_10 = 19
gpio_sw_60 = 13
gpio_sw_res = 6
gpio_sw_st = 5

interval = 0.3

################

# displyas set up
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_led, GPIO.OUT)
GPIO.setup(gpio_sw_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_sw_10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_sw_60, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_sw_res, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_sw_st, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(gpio_led, 0) 

min = 0
status = 0
pressed_time = time.time()


def show_min(min):
    with canvas(device, dither=True) as draw:
        draw.text((10, 20), "Exposure time...", fill="white")
        draw.text((10, 40), str(min) + " min", fill="white")


show_min(min)


while True:
    if (GPIO.input(gpio_sw_1) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 1
        status = 1
        # print(min)
        show_min(min)
        pressed_time = time.time()
    
    elif (GPIO.input(gpio_sw_10) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 10
        status = 1
        # print(min)
        show_min(min)
        pressed_time = time.time()
    
    elif (GPIO.input(gpio_sw_60) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 60
        status = 1
        # print(min)
        show_min(min)
        pressed_time = time.time()

    elif (GPIO.input(gpio_sw_res) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min = 0
        status = 1
        # print(min)
        show_min(min)
        pressed_time = time.time()

    elif (GPIO.input(gpio_sw_st) == 0):
        GPIO.output(gpio_led, 1) 

        with canvas(device, dither=True) as draw:
            draw.text((10, 20), "Now recording...", fill="white")
            draw.text((10, 40), str(min) + " min", fill="white")

        ##################
        ### deeplabcut ###
        ##################
        
        break

    else:
        status = 0


time.sleep(10)

GPIO.cleanup(gpio_led)
GPIO.cleanup(gpio_sw_1)
GPIO.cleanup(gpio_sw_10)
GPIO.cleanup(gpio_sw_60)
GPIO.cleanup(gpio_sw_res)
GPIO.cleanup(gpio_sw_st)
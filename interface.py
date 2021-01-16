import RPi.GPIO as GPIO 
import time

###############

gpio_led = 22
gpio_sw_1 = 26
gpio_sw_10 = 19
gpio_sw_60 = 13
gpio_sw_res = 6
gpio_sw_st = 5

interval = 0.3

#################

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

while True:
    if (GPIO.input(gpio_sw_1) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 1
        status = 1
        print(min)
        pressed_time = time.time()
    
    elif (GPIO.input(gpio_sw_10) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 10
        status = 1
        print(min)
        pressed_time = time.time()
    
    elif (GPIO.input(gpio_sw_60) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min += 60
        status = 1
        print(min)
        pressed_time = time.time()

    elif (GPIO.input(gpio_sw_res) == 0) & (status == 0) & (time.time() - pressed_time > interval):
        min = 0
        status = 1
        print(min)
        pressed_time = time.time()

    elif (GPIO.input(gpio_sw_st) == 0):
        GPIO.output(gpio_led, 1) 

        ##################
        ### deeplabcut ###
        ##################
        break

    else:
        status = 0
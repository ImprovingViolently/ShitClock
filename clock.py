#---------------------------------------
#				CREDITS					
#---------------------------------------
#This project uses libraries from
#https://github.com/T-622/RPI-PICO-I2C-LCD

#Imports

import utime
import time

from time import sleep, time
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#I2C Variables

I2C_ADDR	 = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

#LCD drivers

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=40000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#Displays on boot

def Boot():
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("  mWatchOS 0.1  ")
    lcd.move_to(0,1)
    lcd.putstr("(C) MSG 24/1/22")
    sleep(3)

#Main loop; displays time and periodically flashes the date

def Main():
    while 1==1:
        Time()
        for i in range(179):
            lcd.move_to(2,1)
            lcd.putstr(str(TimeParse()))
            if TimeParse()[2] == 0:
                lcd.move_to(0,1)
                lcd.putstr("                ")
                sleep(0.9)
        Date()
        lcd.putstr(str(DateParse()))
        sleep(3)

#Changes the heading

def Time():
    lcd.clear()
    lcd.putstr("The Current Time")
    lcd.move_to(2,1)
    
def Date():
    lcd.clear()
    lcd.putstr("The Current Date")
    lcd.move_to(1,1)

#Parses from sus tuple format to readable not sus format

def TimeParse():
    raw_tuple = utime.localtime(time())
    clock_list = list(raw_tuple)
    indices=[0,1,2,6,7]
    for i in sorted(indices, reverse=True):
        del clock_list[i]
    clock_tuple = tuple(clock_list)
    return clock_tuple

def DateParse():
    raw_tuple = utime.localtime(time())
    clock_list = list(raw_tuple)
    indices=[3,4,5,6,7]
    for i in sorted(indices, reverse=True):
        del clock_list[i]
    clock_tuple = tuple(clock_list)
    return clock_tuple

Boot()
Time()
lcd.putstr(str(TimeParse()))
sleep(1)
Date()
lcd.putstr(str(DateParse()))
Main()

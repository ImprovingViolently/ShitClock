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

#Global Variables

State = 0

#Displays on boot

def Boot():
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("  mWatchOS 0.2  ")
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
            Alerts()
            if TimeParse()[2] == 0:
                lcd.move_to(0,1)
                lcd.putstr("                ")
        Date()
        for i in range(59):
            lcd.move_to(1,1)
            lcd.putstr(str(DateParse()))
            Alerts()

#Alerts are checked once per cycle
        
def Alerts():
    if TimeParse()[0] == 0 and TimeParse()[1] == 0 and TimeParse()[2] <= 1:
        AlertMessage()
        lcd.putstr("DefaultAlertMesg")
        sleep(10)
        Main()

#Changes the heading

def AlertMessage():
    lcd.clear()
    lcd.putstr("   New Alert    ")
    lcd.move_to(0,1)

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

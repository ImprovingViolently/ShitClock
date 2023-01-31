#---------------------------------------
#				CREDITS					
#---------------------------------------
#This project uses libraries from
#https://github.com/T-622/RPI-PICO-I2C-LCD

#Imports

import urequests
import utime
import time
import network
import _thread

from time import sleep, time
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

from SCDebug import *

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
    lcd.putstr("  mWatchOS 0.3  ")
    lcd.move_to(0,1)
    lcd.putstr("(C) MDRT 31/1/23")
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
        for i in range(29):
            lcd.move_to(1,1)
            lcd.putstr(str(DateParse()))
            Alerts()

#Sequence; runs once on boot, used for debugging.

def Sequence():
    Connect()
    print("db1 Connect Success")
    _thread.start_new_thread(MultithreadedTest, ())
    TestQuery()
    Boot()
    print("db4 Boot Success")
    Main()

#Establishes internet connection

def Connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    ssid      = 'TelstraA5357B'
    password  = 'bkbuf78bxd'
    wlan.connect(ssid, password)

#Alerts are checked once per cycle
        
def Alerts():
    if TimeParse()[0] == 14 and TimeParse()[1] == 20 and TimeParse()[2] <= 1:
        AlertMessage()
        lcd.putstr("Test")
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
    raw_tuple = utime.localtime(utime.time())
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

Sequence()

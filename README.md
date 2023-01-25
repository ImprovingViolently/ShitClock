# What is ShitClock?

ShitClock is possibly my most tacky project yet, consisting of the following components:

- Raspberry Pi Pico W
- 1602 LCD display w/ I2C backpack 
- 4x AA batteries
- 1x N4001 Diode
- 1x Lost Will to Live

I have used ShitClock as an avenue to develop my MicroPython skills, soldering skills and to step out of my comfort zone with physical electronics.

## Features

This project will be iterated upon as time passes and more resources become available, but as of now, the feature set includes:

- Time display/keeping
- Date display
- Boot sequence

Planned features and components include but are not limited to:

- Temperature sensor and display mode
- Bluetooth functionality
- Mode toggle button
- Display toggle button
- Custom PCB
- 3D printable case

# How To Use.

## Installing Display Drivers

The below instructions are provided for https://github.com/T-622/RPI-PICO-I2C-LCD

> 1. Download all 3 .py files included.
> 2. Open Thonny IDE with the 3 files
> 3. Change the default pins to the ones used in your implementation
> 4. DO NOT EDIT FILE NAMES!
> 5. In Thonny, go to top menu File => Save Copy => Raspberry Pi Pico and save each file to the board with the same name as downloaded and with a .PY extension when saving it to the board.
> 6. Switch to the pico_i2c_lcd_test.py (this is the main file) and click run. This should be able to initalize the LCD display if settings are right.

When changing the default pins to the ones used in your implementation, ShitClock uses pins 0 and 1, and maintains the default address.

## Installing mWatchOS

1. Download clock.py.
2. Open clock.py in Thonny and download onto the Pi Pico.
3. Run clock.py 

# Assembly Instructions

Currently, the only existing model, the ShitClockA is assembled on a breadboard.

Assembly instructions will be available in the near future including (as iterations are made, PCB schematics and other useful bits)

# How To add Alerts.

Alerts can be added by using an if statement in the Alerts() function as exampled in the following:

> def Alerts():  
> if TimeParse()[0] == 0 and TimeParse()[1] == 0 and TimeParse()[2] <=1:
>   
>   AlertMessage()
>   
>   lcd.putstr("Test")
  
The above if statement has 3 parameters, but is capable of date specific parameters also. 

> TimeParse()[2]

The above is a necessary parameter in any Alert, as it prevents the Alert from being called multiple times per minute. 
Alerts must be minute specific otherwise unintended behaviour will occur.
Alerts should also end with a call to Main(), in order to maintain consistency.

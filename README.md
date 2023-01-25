# What is ShitClock?

I made a shitty clock (first micropython project, have mercy on me.)

# How To add Alerts

Alerts can be added by using an if statement in the Alerts() function as exampled in the following:

> def Alerts():  
> if TimeParse()[0] == 0 and TimeParse()[1] == 0 and TimeParse()[2] <=1:
>   AlertMessage()
>   lcd.putstr("Test")
  
The above if statement has 3 parameters, but is capable of date specific parameters also. 

> TimeParse()[2]

The above is a necessary parameter in any Alert, as it prevents the Alert from being called multiple times per minute. 
Alerts must be minute specific otherwise unintended behaviour will occur.
Alerts should also end with a call to Main(), in order to maintain consistency.

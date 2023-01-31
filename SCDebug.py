#Imports

import urequests
import time

#Tests internet requests

def TestQuery():
    r = urequests.get("https://www.google.com")
    print(r.content)
    r.close()
    print("TestQuery Ran Successfully")

#Tests multithreaded functionality

def MultithreadedTest():
    sus = 1
    print("sus", sus)
    sus += 1
    print("MultithreadedTest Ran Successfully")

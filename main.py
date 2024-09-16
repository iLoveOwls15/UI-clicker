import pyautogui as pg
import numpy as pd 
import time 

def set_cps(cps):
    cps = int(input("Enter Clicks per second: "))
    if cps > 99:
        raise Exception("Below 100") 
    if cps > 0:
        return cps
    

#def engage_key(option):

#def disengage_key(self):


#def quit(self):
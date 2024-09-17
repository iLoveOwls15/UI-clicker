import pyautogui as pg
import numpy as pd 
import time 
import tkinter

def set_cps(cps):
    cps = int(input("Enter Clicks per second: "))
    if cps > 99:
        raise Exception("Below 100") 
    if cps > 0:
        return cps
    

def button_clickk():
    print("")

#def engage_key(option):


#def disengage_key(self):


#def quit(self):
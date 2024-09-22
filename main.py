import pyautogui as pg
import numpy as pd 
import time 
import tkinter as tk
import interface
from interface import cps, hotkey, stop
global running 
running = False

def startup():

    hotkey = hotkey.lower()
    stop = stop.lower()

    key_mapping = {
        "left": pg.leftClick,
        "right": pg.rightClick,
        "middle": pg.middleClick,
        "up": pg.mouseUp,
        "down": pg.mouseDown,
        "home": pg.HOME,
        "end": pg.END,
        "insert": pg.INSERT,
        "delete": pg.DELETE,
        "f1": pg.F1,
        "f2": pg.F2,
        "f3": pg.F3,
        "f4": pg.F4,
        "f5": pg.F5,
        "f6": pg.F6,
        "f7": pg.F7,
        "f8": pg.F8,
        "f9": pg.F9,
        "f10": pg.F10,
        "f11": pg.F11,
        "f12": pg.F12,

            }
    hotkey_obj = key_mapping.get(hotkey)
    stop_obj = key_mapping.get(stop)

    if hotkey_obj is None or stop_obj is None:
        print("error")
        return
    
    if hotkey.click():
        pg.click(1/cps)
        time.sleep(1/cps)
    elif hotkey.click():
        quit()

    

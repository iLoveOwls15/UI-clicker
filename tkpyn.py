import pynput
import tkinter as tk
import tkinter.ttk as ttk
from pynput import keyboard
from pynput.mouse import Button, Controller
import time

# GUI startup
root = tk.Tk()
root.geometry("460x225")
root.title("Auto Clicker")
root.resizable(False, False)

# Default settings
CLICKS_PER_SECOND = 1
mouse_input = Button.left
start_hotkey = keyboard.Key.f1
stop_hotkey = keyboard.Key.f2
flag = True
click_count = 0
start_time = time.time()

mouse_button_list = {0: Button.left,
                     1: Button.right,
                     2: Button.middle
                        }
                     

key_list = {
        0: keyboard.Key.f1,
        1: keyboard.Key.f2,
        2: keyboard.Key.f3,
        3: keyboard.Key.f4,
        4: keyboard.Key.f5,
        5: keyboard.Key.f6,
        6: keyboard.Key.f7,
        7: keyboard.Key.f8,
        8: keyboard.Key.f9,
        9: keyboard.Key.f10,
        10: keyboard.Key.f11,
        11: keyboard.Key.f12,
        12: "1",
        13: "2",
        14: "3",
        15: "4",
        16: "5",
        17: "6",
        18: "7",
        19: "8",
        20: "9",
        21: "0",
    }

# User mouse controller
mouse = Controller()

# Quit button function
def button_quit():
    root.destroy()

def start_key(do_nothing):
    do_nothing()

mouse_button_frame = tk.Frame(root)
mouse_button_frame.pack()
label_mouse_button = ttk.Label(mouse_button_frame, text="Mouse button: Left")
label_mouse_button.grid(column=1, row=0)
mouse_button_index = ttk.Combobox(mouse_button_frame, values=list(mouse_button_list.values()), state="readonly")
mouse_button_index.grid(column=1, row=1)
mouse_button_index.current(0)
ttk.Button(mouse_button_frame, text="Set", command=mouse_button_list).grid(column=2, row=1)


key_frame = tk.Frame(root)
key_frame.pack()
label_start = ttk.Label(key_frame, text="Start key: F1")
label_start.grid(column=1, row=0)
key_start_index = ttk.Combobox(key_frame, values=list(key_list.values()), state="readonly")
key_start_index.grid(column=1, row=1)
key_start_index.current(0)
ttk.Button(key_frame, text="Set", command=lambda: set_key('start')).grid(column=2, row=1)

label_stop = ttk.Label(key_frame, text="Stop key: F2")
label_stop.grid(column=1, row=2)
key_stop_index = ttk.Combobox(key_frame, values=list(key_list.values()), state="readonly")
key_stop_index.grid(column=1, row=3)
key_stop_index.current(1)
ttk.Button(key_frame, text="Set", command=lambda: set_key('stop')).grid(column=2, row=3)


timer_label = ttk.Label(root, text="Time elapsed: 0s")
timer_label.pack()
click_count_label = ttk.Label(root, text="Click count: 0")
click_count_label.pack()

# Adding a quit button
quit_button = ttk.Button(root, text="Quit", command=button_quit)
quit_button.pack(pady=10)

# Start the GUI loop

root.mainloop()
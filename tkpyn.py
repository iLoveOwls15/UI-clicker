import pynput
import tkinter as tk
import tkinter.ttk as ttk
from pynput import keyboard
from pynput.mouse import Button, Controller
import time

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
    }

def click_loop():
    global click_count
    if not flag:
        mouse.press(mouse_input)
        mouse.release(mouse_input)

        click_count += 1
        click_count_label.config(text=f"Click count: {click_count}")
        # Calculate the delay based on CPS
        delay = int(1000 / CLICKS_PER_SECOND)  # Delay in milliseconds
        root.after(delay, click_loop)


def on_press(key):
    global flag, start_time
    if key == start_hotkey and flag:
        flag = False
        start_time = time.time()
        click_loop()
    elif key == stop_hotkey:
        flag = True
    elif key == button_quit:
        root.destroy()

def set_time():
    global CLICKS_PER_SECOND
    try:
        # Convert time_string to float and use it as CPS
        new_cps = float(time_string.get())
        if new_cps > 0:
            CLICKS_PER_SECOND = new_cps
            label_time.config(text=f"CPS: {CLICKS_PER_SECOND}(s)")
    except ValueError:
        pass
def set_mouse_button():
    global CLICKS_PER_SECOND

    mouse_input = mouse_button_list.get(mouse_button_index.current(), Button.left)
    label_mouse_button.config(text=f"Mouse button: {mouse_input.name.title()}")

def set_key(key_type):
    global start_hotkey, stop_hotkey
    if key_type == 'start':
        # Update the start_hotkey with the new selected key
        start_hotkey = key_list.get(key_start_index.current(), keyboard.Key.f1)
        label_start.config(text=f"Start key: {start_hotkey.name.title()}")
    elif key_type == 'stop':
        stop_hotkey = key_list.get(key_stop_index.current(), keyboard.Key.f2)
        label_stop.config(text=f"Stop key: {stop_hotkey.name.title()}")
        flag = True
        reset_ui()

def reset_ui():
    click_count_label.config(text=f"Click count: 0")



def button_quit():
    root.destroy()
# GUI setup
root = tk.Tk()
root.title("AutoClicker")
root.geometry("300x280")
root.resizable(False, False)

#cps selection
time_frame = tk.Frame(root)
time_frame.pack()
label_time = ttk.Label(time_frame, text="Clicks per second: ")
label_time.grid(column=1, row=0)
time_string = tk.StringVar(value="1")
tk.Entry(time_frame, textvariable=time_string, width=18).grid(column=1, row=1)
ttk.Button(time_frame, text="Set", command=set_time).grid(column=2, row=1)
#Mouse button selection
mouse_button_frame = tk.Frame(root)
mouse_button_frame.pack()
label_mouse_button = ttk.Label(mouse_button_frame, text="Mouse button: Left")
label_mouse_button.grid(column=1, row=0)
mouse_button_index = ttk.Combobox(mouse_button_frame, values=list(mouse_button_list.values()), state="readonly")
mouse_button_index.grid(column=1, row=1)
mouse_button_index.current(0)
ttk.Button(mouse_button_frame, text="Set", command=set_mouse_button).grid(column=2, row=1)
#start selection
key_frame = tk.Frame(root)
key_frame.pack()
label_start = ttk.Label(key_frame, text="Start key: F1")
label_start.grid(column=1, row=0)
key_start_index = ttk.Combobox(key_frame, values=list(key_list.values()), state="readonly")
key_start_index.grid(column=1, row=1)
key_start_index.current(0)
ttk.Button(key_frame, text="Set", command=lambda: set_key('start')).grid(column=2, row=1)
#stop selection
label_stop = ttk.Label(key_frame, text="Stop key: F2")
label_stop.grid(column=1, row=2)
key_stop_index = ttk.Combobox(key_frame, values=list(key_list.values()), state="readonly")
key_stop_index.grid(column=1, row=3)
key_stop_index.current(1)
ttk.Button(key_frame, text="Set", command=lambda: set_key('stop')).grid(column=2, row=3)
#click count
click_count_label = ttk.Label(root, text="Click count: 0")
click_count_label.pack()
quit_button = ttk.Button(root, text="Quit", command=button_quit)
quit_button.pack(pady=10)
#keyboard and controller listener
mouse = Controller()
key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

root.mainloop()
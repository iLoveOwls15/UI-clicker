import pyautogui as pg
import time
import keyboard
import interface
import threading  # Added threading to avoid blocking the Tkinter event loop

global running  # Keep running as global

def startup(cps, hotkey, stop):
    global running  # Declare running as global here to modify it
    hotkey = hotkey.lower()
    stop = stop.lower()

    def auto_click():
        while running:
            if keyboard.is_pressed(stop):
                running = False
                break
            if keyboard.is_pressed(hotkey):
                pg.click()
                time.sleep(1 / cps)

    def start_auto_click():
        global running
        running = True
        threading.Thread(target=auto_click).start()  # Run auto_click in a separate thread

    start_auto_click()

def main():
    # Pass the `startup` function as a callback to the UI
    interface.ui(startup)

if __name__ == "__main__":
    main()


import pyautogui as pg
import time
import threading
import interface
global running  # Keep running as global

def startup(cps, hotkey, stop):
    global running  # Declare running as global here to modify it
    hotkey = hotkey.lower()
    stop = stop.lower()

    def auto_click():
        global running  # Declare running as global here to modify it
        while running:
            if stop in pg.position():
                running = False
                break
            if hotkey in pg.position():
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
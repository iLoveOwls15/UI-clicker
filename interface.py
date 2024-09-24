import tkinter as tk

global running
# Define the callback function to be set externally
run_callback = None

def handle_hotkey(event):
    if event.type == tk.EventType.KeyPress:
        hotkey_entry.delete(0, tk.END)
        hotkey_entry.insert(0, event.keysym)
        print(f"Key pressed: {event.keysym}")

    elif event.type == tk.EventType.ButtonPress:
        hotkey_entry.delete(0, tk.END)
        mouse_button = {1: "Left Click", 2: "Middle Click", 3: "Right Click"}
        hotkey_entry.insert(0, mouse_button.get(event.num, "Unknown Mouse Button"))
        print(f"Mouse button clicked: {mouse_button.get(event.num, 'Unknown Mouse Button')}")

def handle_disable_key(event):
    if event.type == tk.EventType.KeyPress:
        disable_entry.delete(0, tk.END)
        disable_entry.insert(0, event.keysym)
        print(f"Key pressed: {event.keysym}")

    elif event.type == tk.EventType.ButtonPress:
        disable_entry.delete(0, tk.END)
        mouse_button = {1: "Left Click", 2: "Middle Click", 3: "Right Click"}
        disable_entry.insert(0, mouse_button.get(event.num, "Unknown Mouse Button"))
        print(f"Mouse button clicked: {mouse_button.get(event.num, 'Unknown Mouse Button')}")

# This function gets called when the "Run" button is pressed
def button_run():
    cps = int(cps_entry.get())
    hotkey = hotkey_entry.get()
    stop = disable_entry.get()

    if run_callback:  # Check if the callback is set
        run_callback(cps, hotkey, stop)  # Pass the input to the callback

def ui(callback):
    global cps_entry, hotkey_entry, disable_entry, run_callback

    run_callback = callback  # Set the callback function

    root = tk.Tk()
    root.geometry("415x150")
    root.title("Auto Clicker")
    
    cps_label = tk.Label(root, text="Enter CPS:   ")
    cps_label.grid(row=0, column=0, padx=0, pady=0,sticky="w")
    cps_entry = tk.Entry(root)
    cps_entry.grid(row=0, column=1, padx=0, pady=0,sticky="w")

    hotkey_label = tk.Label(root, text="HotKey:       ")
    hotkey_label.grid(row=1, column=0, padx=0, pady=0, sticky="w")
    hotkey_entry = tk.Entry(root)
    hotkey_entry.grid(row=1, column=1, padx=0, pady=0, sticky="w")

    disable_label = tk.Label(root, text="Disable Key:")
    disable_label.grid(row=2, column=0, padx=0, pady=0, sticky="w")
    disable_entry = tk.Entry(root)
    disable_entry.grid(row=2, column=1, padx=0, pady=0, sticky="w")

    hotkey_widget = tk.Label(root, text="Click here for Hotkey/Mouse Button:", bg="lightgray", width=30)
    hotkey_widget.grid(row=1, column=2)
    hotkey_widget.bind("<KeyPress>", handle_hotkey)
    hotkey_widget.bind("<ButtonPress>", handle_hotkey)
    hotkey_widget.focus_set()
    hotkey_widget.bind("<Enter>", lambda e: hotkey_widget.focus_set())

    disable_widget = tk.Label(root, text="Click here for Disable Key:", bg="lightgray", width=30)
    disable_widget.grid(row=2, column=2, sticky="w")
    disable_widget.bind("<KeyPress>", handle_disable_key)
    disable_widget.bind("<ButtonPress>", handle_disable_key)
    disable_widget.bind("<Enter>", lambda e: disable_widget.focus_set())

    br = tk.Button(root, text="Run", command=button_run)
    br.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    def button_quit():
        root.destroy()

    bq = tk.Button(root, text="Quit", command=button_quit)
    bq.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    root.configure(bg="skyblue")
    root.mainloop()

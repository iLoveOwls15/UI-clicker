import tkinter as tk
from main import set_cps, button_clickk  # Assuming you still want to import this

# Create the main application window
root = tk.Tk()
root.geometry("400x200")
root.title("Auto Clicker")

cps_label = tk.Label(root, text="Enter CPS:")
cps_label.grid(row=0, column=0, padx=0, pady=0, sticky="w")
cps_entry = tk.Entry(root)
cps_entry.grid(row=0, column=1, padx=0, pady=0)

hotkey_label = tk.Label(root, text="Enter Hot Key:")
hotkey_label.grid(row=1, column=0, padx=0, pady=0, sticky="w")
hotkey_entry = tk.Entry(root)
hotkey_entry.grid(row=1, column=1, padx=0, pady=0)

disable_label = tk.Label(root, text = "Enter deactivation key (Can be same): ")
disable_label.grid(row = 2, column = 0, padx=0, pady=0, sticky = "w")
disable_entry = tk.Entry(root)
disable_entry.grid(row=2, column=1, padx=0, pady=0)

    
button = tk.Button(root, text="Run", command=button_clickk)
button.grid(row=3, column=0, padx=0, pady=0, sticky="w")

root.mainloop()

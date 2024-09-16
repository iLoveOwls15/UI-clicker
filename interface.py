
from appJar import gui
from main import set_cps 

app = gui() 

app.setSize("600x300")
app.addLabel("cps_label", "Enter CPS:", row=0, column=0)
app.addEntry("cps", row=0, column=1)

# Adding "Enter Hot Key:" label and entry in the second row, first column
app.addLabel("hotkey_label", "Enter Hot Key:", row=1, column=0)
app.addEntry("hotkey", row=1, column=1)
app.go()
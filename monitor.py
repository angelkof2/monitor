#let me know if importing just part of the libraries makes a performance difference in PY
from psutil import cpu_percent
from psutil import virtual_memory
from tkinter import TRUE
from tkinter import Tk
from tkinter.font import Font
from tkinter import Label
from tkinter import LEFT

def cpumonitor():
    monitorcpu = cpu_percent(interval=1,percpu=True)
    var01 = ""
    for i in range(len(monitorcpu)):
        var01 = var01 + "CPU" + str(i) + "=" + str(monitorcpu[i]) + "%\n"      
    return var01

def rammonitor():
    return "RAM:" + str(virtual_memory().percent) + "%"

#Window
root = Tk()
root.wm_attributes("-transparentcolor","white","-topmost",1) #delete "'-topmost', 1" if you don't want it on top of everything
root.geometry("170x200")
root.config(bg="white")
root.overrideredirect(TRUE)

monitorfont = Font(size=20, family="Bahnschrift SemiBold")

#LABELS
cputxt = Label(root,text=cpumonitor(),font=monitorfont,bg="white",fg="#FFFFFE", justify=LEFT)
cputxt.pack()
ramtxt = Label(root,text=rammonitor(),font=monitorfont,bg="white",fg="#FFFFFE", justify=LEFT)
ramtxt.pack()

while True:
    cputxt.config(text=cpumonitor())
    cputxt.update()
    ramtxt.config(text=rammonitor())
    ramtxt.update()

root.mainloop()

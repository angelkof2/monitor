import psutil
from tkinter import *
from tkinter.font import Font

def cpumonitor():
    monitorcpu = psutil.cpu_percent(interval=1,percpu=True)
    var01 = ""
    for i in range(len(monitorcpu)):
        var01 = var01 + "CPU" + str(i) + "=" + str(monitorcpu[i]) + "%\n"      
    return var01

def rammonitor():
    return "RAM:" + str(psutil.virtual_memory().percent) + "%"

root = Tk()
root.wm_attributes("-transparentcolor","white")
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
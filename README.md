# monitor
Windows monitor widget written in Python. The main goal is to use the less resources possible (RAM,CPU).

After 10 years without programming, this is my first Python application, so I'm a little bit rusty.

Let me know if importing just part of the libraries makes a performance difference in PY. This are the changes that i have implemented:

import psutil ---> from psutil import cpu_percent
                   from psutil import virtual_memory
                   
from tkinter import * ---> from tkinter import Tk
                           from tkinter import Label
                           from tkinter import TRUE
                           from tkinter import LEFT

I have created the .exe using pyinstaller.exe and the output weight the same and i think it consumes the same amount of resources.

All insights are welcome.

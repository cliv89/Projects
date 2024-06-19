from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('Local Time')

def time():
    localTime = strftime('%b%d/%Y %I:%M:%S %p')
    clock.config(text = localTime)
    clock.after(1000, time)
    
clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'dark blue',
                                foreground = 'white')

clock.pack(anchor = 'center')
time()

mainloop()
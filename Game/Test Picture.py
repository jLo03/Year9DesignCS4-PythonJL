import time
import os
from tkinter import *
import threading

root = Tk()

frames = [PhotoImage(file='Sword.gif',format = 'gif -index %i' %(i)) for i in range(10)]

def update(ind):
    frame = frames[ind]
    ind += 1
    time.sleep(0.2)
    label.configure(image=frame)
    root.after(6, update, ind)

label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()

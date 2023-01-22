#Name: Keybind Reminder
#Author: Carlo Bisda
#Version: 1.0.1
#License: MIT
#Link: https://github.com/carlobisda

from tkinter import *

ws = Tk()
ws.title("@zupercb_siliconTor")
ws.geometry("350x700")
ws['bg']='#444444' #background color feature
ws.attributes("-alpha", 0.7) #opacity default

txtarea=Text(ws, width=40, height=40)
txtarea.pack(pady=1)

with open("keybinds.md", 'r') as tf:
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws.mainloop()

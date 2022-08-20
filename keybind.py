#create a screenlet to display keyboard hotkeys, similar to archbangs
from tkinter import *

ws = Tk()
ws.title("@zupercb_siliconTor")
ws.geometry("350x400")

txtarea=Text(ws, width=40, height=20)
txtarea.pack(pady=1)

with open("keybinds.md", 'r') as tf:
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws.mainloop()

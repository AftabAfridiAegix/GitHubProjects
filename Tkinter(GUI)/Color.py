from tkinter import *
from tkinter import colorchooser #sub module
window = Tk()
window.geometry("420x420")

def click():
    color = colorchooser.askcolor()
    print(color)
    # 
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex) # change background color

button = Button(window, text = "Click Me", command = click)
button.pack() # put button inside window

window.mainloop()


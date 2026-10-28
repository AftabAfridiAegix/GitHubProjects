from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

def openFile():
    filepath = filedialog.askopenfilename(initialdir = "")
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
color = colorchooser.askcolor()
print(color)

colorHex = color[1]
print(colorHex)
window.config(bg=colorHex)
button = Button(window,
                text = "Open", command = openFile)
button.pack()
window.mainloop()

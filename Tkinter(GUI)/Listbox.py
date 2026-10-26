from tkinter import *

window = Tk()
window.title("Listbox Examole")
window.geometry("300x300")

listbox = Listbox(window)

listbox.insert(1, "Python")
listbox.insert(2, "java")
listbox.insert(3, "c++")
listbox.insert(4, "javascript")


listbox.pack()

window.mainloop()

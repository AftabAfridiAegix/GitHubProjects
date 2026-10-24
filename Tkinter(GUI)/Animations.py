from tkinter import *
from PIL import Image, ImageTk
import time

Width = 500
Height = 500
xVelocity = 1
yVelocity = 1
window = Tk()


canvas = Canvas(window,width = Width, height= Height)
canvas.pack()
photo_image = PhotoImage(file = r"C:\Users\hp\Desktop\Programming\Python\Tkinter(GUI)\pic.png")
my_image = canvas.create_image(0,0,image = photo_image, anchor = NW)

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0]>Width or coordinates[0]<0):
        xVelocity = -xVelocity 
    canvas.move(my_image,xVelocity,0)
    window.update()
    time.sleep(0.01)

window.mainloop()

















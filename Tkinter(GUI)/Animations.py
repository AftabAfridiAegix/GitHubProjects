
from tkinter import *
import time

Width = 500
Height = 500
xVelocity = 1
window = Tk()

canvas = Canvas(window, width=Width, height=Height)
canvas.pack()

photo_image = PhotoImage(file=r"C:\Users\hp\Desktop\GitHubProjects\Tkinter(GUI)\pic.png")
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

while True:
    coordinates = canvas.coords(my_image)

    if coordinates[0] >= Width - photo_image.width():
        xVelocity = -1

    elif coordinates[0] <= 0:
        xVelocity = 1

    canvas.move(my_image, xVelocity, 0)
    window.update()
    time.sleep(0.01)

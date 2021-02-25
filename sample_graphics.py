from tkinter import *
import math as m
from time import sleep

# Thanks to KidsCanCode
# tkinter is the tk interface graphics package

root = Tk()  # Initializes the tk system with a tk object
canvas = Canvas(root, width=500, height=400)  # Makes a canvas to draw on
root.title('Circle Weaving')  # Create a title
canvas.pack()  # We're done with settings, go ahead and make window.

for i in range(180):
    # Calculate coordinates for squares that swirl.
    x1 = 150 * m.cos(i) + 250
    y1 = 150 * m.sin(i) + 200
    
    x2 = -150 * m.cos(i) + 250
    y2 = -150 * m.sin(i) + 200
    sleep(0.01)    
    canvas.create_rectangle(x1, y1, x2, y2)
    root.update()

canvas.mainloop()  # Show the window and don't do anything else.



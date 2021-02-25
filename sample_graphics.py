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
    sleep(0.005)    
    canvas.create_rectangle(x1, y1, x2, y2)
    root.update()


for i in range(0, 720):
    j = int(i/3)
    x1 = 50 * m.cos((360 - i)/(2 * m.pi)) + j
    y1 = 50 * m.sin((i)/(2* m.pi)) + 300
    x2 = 50 * m.cos((270 - i)/(2* m.pi)) + j
    y2 = 50 * m.sin((i + 90)/(2* m.pi)) + 300
    x3 = 50 * m.cos((180 - i)/(2* m.pi)) + j
    y3 = 50 * m.sin((i + 180)/(2* m.pi)) + 300
    x4 = 50 * m.cos((90 - i)/(2* m.pi)) + j
    y4 = 50 * m.sin((i + 270)/(2* m.pi)) + 300

    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, outline="red")
    canvas.create_polygon(j, 300, 50 + j, 305, 50 + j, 295, outline="black", fill="black")
    canvas.create_oval(j + 45, 295, j+ 55, 305, fill="blue")
    root.update()    


canvas.mainloop()  # Show the window and don't do anything else.



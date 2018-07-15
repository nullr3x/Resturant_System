from tkinter import *

# create the canvas, size in pixels
canvas = Canvas(width=300, height=200, bg='white')
canvas.grid(row = 0, column = 0, rowspan = 11, columnspan = 3)
# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='6.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(1100, 10, image=gif1, anchor=NW)

# run it ...
mainloop()

from tkinter import *

root = Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="#d9d9d9")

background_image = PhotoImage(file="6.png")
background_image = image.resize((250, 250), Image.ANTIALIAS)
background = Label(root, image=background_image, bd=0)
background.pack()

root.mainloop()
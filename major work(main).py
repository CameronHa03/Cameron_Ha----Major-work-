from tkinter import *

root = Tk(className="Python window")

# setting size of window
root.geometry("500x200")

bg = PhotoImage(file="background_major.png")

background = Label(root, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)

start_button = Button(root, text="Start")
start_button.pack()

root.mainloop()
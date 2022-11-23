import tkinter as tk
from tkinter import Frame
import utils
import Settings
root=tk.Tk()
#general settings of the window
root.configure(bg='red')
root.geometry(f'{Settings.width}x{Settings.height}')
root.title("Minesweeper")
root.resizable(False,False)

top_frame= Frame(
    root,
    bg='red', 
    width=Settings.width,
    height=utils.height_percentage(25)
)

left_frame= Frame(
    root,
    bg='red'
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
top_frame.place(x=0,y=0)
left_frame.place(x=0,y=utils.height_percentage(25))
center_frame= Frame (
    root,
    bg='red' , 
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(
    x=utils.width_percentage(25),
    y=utils.height_percentage(25),
)



#run the window
root.mainloop()

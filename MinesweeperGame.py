
from tkinter import *
import utils
import Settings
from Cell import cell
root=Tk()
#general settings of the window
root.configure(bg='black')
root.geometry(f'{Settings.width}x{Settings.height}')
root.title("Minesweeper")
root.resizable(False,False)

top_frame= Frame(
    root,
    bg='black', 
    width=Settings.width,
    height=utils.height_percentage(10),
    
    )

game_area= Frame (
    root,
    bg='black' , 
    width=Settings.width,
    height=utils.height_percentage(25)
    )

top_frame.place(x=0,y=0)
game_area.place(
    x=0,
    y=utils.height_percentage(10),
)





for x in range(Settings.grid_size):
    for y in range(Settings.grid_size):
        c=cell(x,y)
        c.create_btn_object(game_area)
        c.cell_btn_object.grid(
            column=x, row=y
        )
cell.create_cell_count_label(top_frame)
cell.cell_count_label_object.place(
    x=0,y=0
)
cell.mines_1() 



root.mainloop()

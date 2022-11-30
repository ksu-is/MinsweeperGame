from tkinter import Button,Label
import random
import Settings
import ctypes
import sys
class cell:
    all = []
    cell_count_label_object= None
    cell_count=Settings.cell_count
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened=False
        self.is_mine_canidate=False
        self.cell_btn_object= None
        self.x = x
        self.y = y  
#append to all list
        cell.all.append(self)

    def create_btn_object(self, location):
        btn=Button (
            location,
            width=3,
            height=1,
            
            )
        btn.bind('<Button-1>',self.left_click ) #left click stuff
        btn.bind('<Button-3>',self.right_click ) # right click stuff
        self.cell_btn_object=btn 

    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{cell.cell_count}",
            width= 10,
            height=1
        )
        cell.cell_count_label_object=lbl



    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mine_length==0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if cell.cell_count==Settings.mines_count:
                 ctypes.windll.user32.MessageBoxW(0,'FEDRICE CONGRATULATES YOU!!!', 'VICTORY',1)

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def cell_by_axis(self, x,y):
        global cell
        #return cell object by x and y
        for cell in cell.all:
            if cell.x== x and cell.y==y:
                return cell
    
    @property
    def surrounding_cells(self):
         cells= [
            self.cell_by_axis(self.x-1,self.y-1),
            self.cell_by_axis(self.x-1,self.y),
            self.cell_by_axis(self.x-1, self.y+1),
            self.cell_by_axis(self.x,self.y-1),
            self.cell_by_axis(self.x+1,self.y-1),
            self.cell_by_axis(self.x+1,self.y),
            self.cell_by_axis(self.x+1,self.y+1),
            self.cell_by_axis(self.x,self.y+1)
        ]
         cells=[cell for cell in cells if cell is not None]
         return cells

    @property
    def surrounding_cells_mine_length(self):
        counter=0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter+=1
        return counter


    def show_cell(self):
        if not self.is_opened:
            cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounding_cells_mine_length)
            if cell.cell_count_label_object:
                cell.cell_count_label_object.configure(
                    text=f"Cells Left:{cell.cell_count}"
                )

            self.is_opened=True
       

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine!!!', 'Game Over',1)
        sys.exit()
        
    
    def right_click(self,event):
        if not self.is_mine_canidate:
            self.cell_btn_object.configure(bg='green')
            self.is_mine_canidate=True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_canidate=False
            

    @staticmethod
    def mines_1():
            bomb_cells=random.sample(
            cell.all, Settings.mines_count
        )
            for bomb_cell in bomb_cells:
                bomb_cell.is_mine=True
            

    def __repr__ (self):
        return f"cell({self.x},{self.y})"

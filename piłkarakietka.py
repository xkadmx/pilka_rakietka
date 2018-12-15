from tkinter import *
import random
import time

class Piłka:
    def __init__(self, płótno, kolor):
        self.płótno = płótno
        self.id = płótno.create_oval(10,10,25,25, fill=kolor)
        self.płótno.move(self.id, 245,100)
    def rysuj(self):
        pass

    
tk = Tk()
tk.title(" Gra")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
płótno = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
płótno.pack()
tk.update()


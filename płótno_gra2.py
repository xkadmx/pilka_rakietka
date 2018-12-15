from tkinter import *
import random
import time

class Piłka:
    def __init__(self, płótno, kolor):
        self.płótno = płótno
        self.id = płótno.create_oval(10,10,25,25, fill = kolor)
        self.płótno.move(self.id, 245,100)
        początek = [-3,-2,-1,1,2,3]
        random.shuffle(początek)
        self.x = początek[0]
        self.y = -3
        self.wysokość_płótna = self.płótno.winfo_height()
        self.szerokość_płótna = self.płótno.winfo_width()

                
    def rysuj(self):
        self.płótno.move(self.id, self.x, self.y)
        pozycja = self.płótno.coords(self.id)
        if pozycja[1] <= 0:
            self.y = 3
        if pozycja[3] >= self.wysokość_płótna:
            self.y = -3
        if pozycja[0] <= 0:
            self.x = 3
        if pozycja[2] >= self.szerokość_płótna:
            self.x = -3


tk=Tk()
tk.title("Gra")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
płótno = Canvas(tk, width=500, height=400, highlightthickness=0)
płótno.pack()
tk.update()



        
piłka = Piłka(płótno, 'red')

while 1:
    piłka.rysuj()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

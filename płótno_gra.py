from tkinter import *
import random
import time

class Piłka:
    def __init__(self, płótno, rakietka,kolor):
        self.płótno = płótno
        self.płótno = rakietka
        self.id = płótno.create_oval(10,10,25,25, fill=kolor)
        self.płótno.move(self.id, 245,100)
        początek = [-3,-2,-1,1,2,3]
        random.shuffle(początek)
        self.x = początek[0]
        self.y = -3
        self.wysokość_płótna = self.płótno.winfo_height()
        self.szerokość_płótna = self.płótno.winfo_width()
        self.upadek_na_ziemię = False
    def trafienie_w_piłkę(self, pozycja):
        pozycja_rakietki = self.płótno.coords(self.rakietka.id)
        if pozycja[2] >= pozycja_rakietki[0] and pozycja[0]<= pozycja_rakietki[2]:
            if pozycja[3]>= pozycja_rakietki[1] and pozycja[3]<= pozycja_rakietki[3]:
                   return True
        return False
               
                           
    def rysuj(self):
        self.płótno.move(self.id, self.x, self.y)
        pozycja = self.płótno.coords(self.id)
        if pozycja[1] <= 0:
            self.y = 3
        if pozycja[3]>=self.wysokość_płótna:
            self.upadek_na_ziemię = True
        if self.trafienie_w_piłkę(pozycja) == True:
            self.y = -3
                
        if pozycja[0] <= 0:
            self.x = 3
        if pozycja[2] >= self.szerokość_płótna:
            self.x = -3

class Rakietka:
    def __init__(self, płótno, kolor):
        self.płótno = płótno
        self.id = płótno.create_rectangle(0,0,100,10, fill=kolor)
        self.płótno.move(self.id,200,300)
        self.x=0
        self.szerokość_płótna = self.płótno.winfo_width()
        self.płótno.bind_all('<KeyPress-Left>', self.przesuń_w_lewo)
        self.płótno.bind_all('<KeyPress-Right>', self.przesuń_w_prawo)

    def rysuj(self):
        self.płótno.move(self.id, self.x, 0)
        pozycja = self.płótno.coords(self.id)
        if pozycja[0] <=0:
            self.x = 0
        elif pozycja[2]>= self.szerokość_płótna:
            self.x=0
                

tk = Tk()
tk.title("Gra")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
płótno = Canvas(tk, width = 500, height = 400, bd=0,
highlightthickness=0)
płótno.pack()
tk.update()

rakietka = Rakietka(płótno, 'blue')
piłka = Piłka(płótno, rakietka, 'red')
while 1:
    if piłka.upadek_na_ziemię == False:
        piłka.rysuj()
        rakietka.rysuj()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    

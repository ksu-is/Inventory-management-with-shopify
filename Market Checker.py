from tkinter import ttk
from tkinter import *
import sqlite3
import os.path


class Market:
    
    def __init__(self):
        self.marketw = Tk()
        self.marketw.title("Market Inventory Checker and Query")
        width = 1400
        height = 780
        screen_width = self.marketw.winfo_screenwidth()
        screen_height = self.marketw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.marketw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.marketw.title("Inventory")
        self.marketw.resizable(0,0)
        self.marketquery = Button(self.marketw,text="Press for Market Query", command=self.MarketGrab)
        self.marketquery.place(x=100,y=200)
        self.marketw.mainloop()
        
    def MarketGrab(self):
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, "Items and products.db")
        self.base = sqlite3.connect(db)

        
        self.cur = self.base.cursor()
        
        self.cur.execute("SELECT * From 'Wild Pack' where ItemQty ")
        self.runner = self.cur.fetchall()
        i=0
        for inventory in self.runner:
            for j in range(len(inventory)):
                e = Entry(self.marketw,width=30,fg='#7B3F00',bg='#FCD667')
                e.grid(row=5,column=j)
                e.insert(END,inventory[j])
            i+=1
        


    """def MarketCheckBox(self):
        self.checkbrook = Checkbutton()
        self.checkpeacht =
        self.checkten =
        self.check ="""

w=Market()
w.base.commit()
w.marketw.mainloop()
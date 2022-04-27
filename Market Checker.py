
from tkinter import ttk
from tkinter import *
import sqlite3
import os.path

test_word = 13
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
        self.marketquery = Button(self.marketw,text="Press for Market Query", command=self.MarketCheckBox)
        self.marketquery.place(x=100,y=200)
        self.Display()
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
        


    def MarketCheckBox(self):
        self.checkboxframe = LabelFrame(self.marketw,height=200,width=600, text= "Check Box For Market Selcetion To Be Queried ")
<<<<<<< Updated upstream
        self.checkboxframe.place(x=10,y=10)
        self.checkbrook = Checkbutton (self.checkboxframe, text= "Brookhaven Farmer's Market", width=20)
=======
        self.checkboxframe.place(x=10,y=35)
        self.checkbrook = Checkbutton (self.checkboxframe, text= "Brookhaven Farmer's Market", height=2 )
>>>>>>> Stashed changes
        self.checkbrook.place(x=10, y=10)
        self.checkpeacht = Checkbutton (self.checkboxframe, text= "Peachtree City Farmer's Market", )
        self.checkpeacht.place(x=10, y=30)
        self.checkten = Checkbutton (self.checkboxframe, text= "Chattanooga Farmer's Market", )
        self.checkten.place(x=10, y=50)
        self.checksuwanee = Checkbutton (self.checkboxframe, text= "Suwanee Farmer's Market", )
        self.checksuwanee.place(x=10, y=70)
<<<<<<< Updated upstream
        self.checkbrook = Checkbutton (self.checkboxframe, text= "Small Events", width=20)
        self.checkbrook.place(x=210, y=10)
        self.checkpeacht = Checkbutton (self.checkboxframe, text= "Medium Events", width=20)
        self.checkpeacht.place(x=210, y=30)
        self.checkten = Checkbutton (self.checkboxframe, text= "Large Events", width=20)
        self.checkten.place(x=210, y=50)
        self.checksuwanee = Checkbutton (self.checkboxframe, text= "Suwanee Farmer's Market", width=20)
=======
        self.checksmalle = Checkbutton (self.checkboxframe, text= "Small Event", )
        self.checksmalle.place(x=210, y=10)
        self.checkmediume = Checkbutton (self.checkboxframe, text= "Medium Event", )
        self.checkmediume.place(x=210, y=30)
        self.checkbige = Checkbutton (self.checkboxframe, text= "Medium Event", )
        self.checkbige.place(x=210, y=50)
        self.checksuwanee = Checkbutton (self.checkboxframe, text= f"Suwanee{test_word} Farmer's Market",)
>>>>>>> Stashed changes
        self.checksuwanee.place(x=210, y=70)
    
    def MarketSum(self):
        pass

    def Display(self):
        self.longframe = LabelFrame(self.marketw, height=550,width=600,text="Total Amounts For Selected Markets")
        self.longframe.place(x=700,y=35)
        self.totalframe = LabelFrame(self.marketw, height=100,width=600,text="Total",bg="white")
        self.totalframe.place(x=700,y=630)

w=Market()

w.marketw.mainloop()
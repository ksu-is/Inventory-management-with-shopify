
from itertools import count
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#import tkinter.ttk as ttkstyle
import sqlite3
import os.path
import tkinter




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
        self.topframe=LabelFrame(self.marketw,width=1400,height=120,bg="#F47F20")
        self.topframe.place(x=0,y=0)
        self.bottomframe=LabelFrame(self.marketw,width=1400,height=120,bg="#F47F20")
        self.bottomframe.place(x=0,y=660)
        #self.marketquery = Button(self.bottomframe,text="Press for Market Query", command=self.MarketCheckBox, bg="#F47F20", relief="flat")
        #self.marketquery.place(x=0,y=0)
        self.additem = Button(self.marketw, text = "Add/Remove Item", height=9, width=8, wraplength=80,)
        self.additem.place(x=9, y=460)
        self.additem = Button(self.marketw, text = "Update Inventory Item", height=9, width=8,wraplength=80,)
        self.additem.place(x=134, y=460)
        self.additem = Button(self.marketw, text = "Update Shopify", height=9, width=8,wraplength=80) 
        self.additem.place(x=259, y=460)
        self.additem = Button(self.marketw, text = "Retrieve From Shopify", height=9, width=8,wraplength=80,)
        self.additem.place(x=382, y=460)
        self.additem = Button(self.marketw, text = "Exit", height=9, width=8,wraplength=80,command=self.__Main_del__)
        self.additem.place(x=504, y=460)
        #self.MarketGrab()
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
                            background = "#7B3F00",
                            foreground = '#FCD667',
                            rowheight = 25,
                            fieldbackground ="#7B3F00")
        self.style.map("Treeview",
                background =[('selected','#FCD667')])
        
        self.tree_frame = Frame(self.marketw)
        self.tree_frame.place(x=620,y=140)
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill=Y)
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set,selectmode='extended')
        self.my_tree.pack
        self.tree_scroll.config(command=self.my_tree.yview)
        self.my_tree['columns'] = ("Item ID", "Item Name", "Unit Price", "Item Type","Item Quantity", "Sale Type")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Item ID",width=50,anchor=W)
        self.my_tree.column("Item Name",width=50,anchor=W)
        self.my_tree.column("Unit Price",width=50,anchor=CENTER)
        self.my_tree.column("Item Type",width=50,anchor=CENTER)
        self.my_tree.column("Item Quantity",width=50,anchor=CENTER)
        self.my_tree.column("Sale Type",width=50,anchor=CENTER)

        self.my_tree.heading("#0",text="",anchor=W)
        self.my_tree.heading("Item ID",text="Item ID",anchor=W)
        self.my_tree.heading("Item Name",text="Item Name",anchor=W)
        self.my_tree.heading("Unit Price",text="Unit Price",anchor=CENTER)
        self.my_tree.heading("Item Type",text="Item Type",anchor=CENTER)
        self.my_tree.heading("Item Quantity",text="Item Quantity",anchor=CENTER)
        self.my_tree.heading("Sale Type",text="Sale Type",anchor=CENTER)

        self.my_tree.tag_configure('oddrow',background='white')
        self.my_tree.tag_configure('evenrow',background='lightblue')

        self.data_frame = LabelFrame(self.marketw, text="test1",height=100,width=200)
        self.data_frame.place(x=620,y=652)

        ID_label = Label(self.data_frame, text= "Item ID")
        ID_label.grid(row=0,column=0,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=0,column=1,padx=10,pady=10)

        ID_label = Label(self.data_frame, text= "Item Name")
        ID_label.grid(row=0,column=2,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=0,column=3,padx=10,pady=10)

        ID_label = Label(self.data_frame, text= "Unit Price")
        ID_label.grid(row=0,column=4,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=0,column=5,padx=10,pady=10) 

        ID_label = Label(self.data_frame, text= "Item Type")
        ID_label.grid(row=1,column=0,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=1,column=1,padx=10,pady=10)

        ID_label = Label(self.data_frame, text= "Item Quantity")
        ID_label.grid(row=1,column=2,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=1,column=3,padx=10,pady=10)

        ID_label = Label(self.data_frame, text= "Sale Type")
        ID_label.grid(row=1,column=4,padx=10,pady=10)
        ID_entry = Entry(self.data_frame)
        ID_entry.grid(row=1,column=5,padx=10,pady=10) 

        
        
        #self.Display()
        self.query_data()
        self.MarketCheckBox()
        self.marketw.mainloop()

    def query_data(self):
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, "Items and products.db")
        self.base = sqlite3.connect(db)
        self.cur = self.base.cursor()
        self.cur.execute("SELECT * FROM Items")
        self.runner = self.cur.fetchall()

        global count
        count = 0

        for inventory in self.runner:
            if count % 2==0:
                self.my_tree.insert(parent='',index='end',iid=count, text='', tag=('evenrow',))
            else:
                self.my_tree.insert(parent='',index='end',iid=count, text='', tag=('oddrow',))
            count+=1

        self.base.commit()
        self.base.close()
        
    def MarketGrab(self):
        
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, "Items and products.db")
        self.base = sqlite3.connect(db)

        
        self.cur = self.base.cursor()
        
        self.cur.execute("SELECT * FROM Items ")
        self.runner = self.cur.fetchall()
        i=0
        for inventory in self.runner:
            for j in range(len(inventory)):
                e = Entry(self.longframe,width=13,fg='#7B3F00',bg='#FCD667')
                e.grid(row=5,column=j)
                e.insert(END,inventory[j])
            i+=1
        
        style=ttk.Style()

        


    def MarketCheckBox(self):
        self.varbrook = tkinter.IntVar(value=1)
        self.checkboxframe = LabelFrame(self.marketw,height=230,width=600, text= "Check Box For Market Selcetion To Be Queried ")
        self.checkboxframe.place(x=10,y=140)
        self.checkbrook = Checkbutton (self.checkboxframe, text= "Brookhaven Farmer's Market",variable=self.varbrook, onvalue=0, offvalue=1 )
        self.checkbrook.place(x=10, y=10)
        self.checkpeacht = Checkbutton (self.checkboxframe, text= "Peachtree City Farmer's Market", )
        self.checkpeacht.place(x=10, y=30)
        self.checkten = Checkbutton (self.checkboxframe, text= "Chattanooga Farmer's Market", )
        self.checkten.place(x=10, y=50)
        self.checksuwanee = Checkbutton (self.checkboxframe, text= "Suwanee Farmer's Market", )
        self.checksuwanee.place(x=10, y=70)
        self.checksmalle = Checkbutton (self.checkboxframe, text= "Alpharetta Farmer's Market", )
        self.checksmalle.place(x=230, y=10)
        self.checkmediume = Checkbutton (self.checkboxframe, text= "Small Event", )
        self.checkmediume.place(x=230, y=30)
        self.checkbige = Checkbutton (self.checkboxframe, text= "Medium Event", )
        self.checkbige.place(x=230, y=50)
        self.checksuwanee = Checkbutton (self.checkboxframe, text= "Big Event",)
        self.checksuwanee.place(x=230, y=70)
        self.totalframe = LabelFrame(self.checkboxframe, height=100,width=574,text="Total",relief='ridge')
        self.totalframe.place(x=10,y=90)
    
    def __Main_del__(self):
        if messagebox.askyesno("Quit", " Leave Inventory?") == True:
            self.marketw.quit()
            exit(0)
        else:
            pass
        
        
    
    #def CheckBoxVal(self):
        


    def MarketSum(self):
        pass

    def Display(self):
        self.longframe = LabelFrame(self.marketw, height=492,width=770,text="Total Amounts For Selected Markets")
        self.longframe.place(x=620,y=140)
        self.totalframebacker = LabelFrame(self.marketw, height=100,width=600,bg="#F47F20",)
        self.totalframebacker.place(x=620,y=670)
        self.MarketGrab()
        
        

    #Market total dictionaries
    class_pack_amnts = {"brookhaven":7, 
                        "peachtree":8, 
                        "chatta":25, 
                        "suwanee":7, 
                        "small":7, 
                        "medium":14, 
                        "big":25, 
                        "alpha":8
    }

    wild_pack_amnts = {"brookhaven":7, 
                        "peachtree":8, 
                        "chatta":25, 
                        "suwanee":7, 
                        "small":7, 
                        "medium":14, 
                        "big":25, 
                        "alpha":8
    }
    

    flavor_pack_amnts = {"brookhaven":7, 
                        "peachtree":8, 
                        "chatta":25, 
                        "suwanee":7, 
                        "small":7, 
                        "medium":14, 
                        "big":25, 
                        "alpha":8
    }

    season_pack_amnts = {"brookhaven":7, 
                        "peachtree":8, 
                        "chatta":25, 
                        "suwanee":7, 
                        "small":7, 
                        "medium":14, 
                        "big":25, 
                        "alpha":8
    }


    #print(test_dict["test_flavor_1"])
    #total = 0
    #for values in test_dict.values():
        #total = total + values
        

    #print(total)

    #def showdata(self):

    #def addindata(self):

        


w=Market()

w.marketw.mainloop()
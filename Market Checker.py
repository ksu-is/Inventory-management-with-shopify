
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
        self.marketw.resizable(True,True)
        #Orange placer
        self.topframe=LabelFrame(self.marketw,width=1400,height=120,bg="#F47F20")
        self.topframe.place(x=0,y=0)
        self.bottomframe=LabelFrame(self.marketw,width=1400,height=120,bg="#F47F20")
        self.bottomframe.place(x=0,y=660)
        #self.marketquery = Button(self.bottomframe,text="Press for Market Query", command=self.MarketCheckBox, bg="#F47F20", relief="flat")
        #self.marketquery.place(x=0,y=0)

        #Buttons under Market Box
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
        self.additem = Button(self.marketw, text = "Select Item", height=9, width=8,wraplength=80,command=self.select_record)
        self.additem.place(x=450, y=460)  
        #self.my_tree.bind("<ButtonRelease-1>",self.select_record) 
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
        
        self.tree_frame = LabelFrame(self.marketw,height=200,width=30)
        self.tree_frame.place(x=665,y=146)
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill=Y)
        self.my_tree = ttk.Treeview(self.tree_frame,yscrollcommand=self.tree_scroll.set,selectmode='extended')
        #self.my_tree.pack()

        

        #Columns and headings for the database table
        self.tree_scroll.config(command=self.my_tree.yview)
        self.my_tree['columns'] = ("Item ID", "Item Name", "Unit Price", "Item Type","Item Quantity", "Sale Type")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Item ID",width=60,anchor=CENTER)
        self.my_tree.column("Item Name",width=175,anchor=CENTER)
        self.my_tree.column("Unit Price",width=60,anchor=CENTER)
        self.my_tree.column("Item Type",width=175,anchor=CENTER)
        self.my_tree.column("Item Quantity",width=60,anchor=CENTER)
        self.my_tree.column("Sale Type",width=175,anchor=CENTER)

        self.my_tree.heading("#0",text="",anchor=W)
        self.my_tree.heading("Item ID",text="Item ID",anchor=CENTER)
        self.my_tree.heading("Item Name",text="Item Name",anchor=CENTER)
        self.my_tree.heading("Unit Price",text="Unit Price",anchor=CENTER)
        self.my_tree.heading("Item Type",text="Item Type",anchor=CENTER)
        self.my_tree.heading("Item Quantity",text="Item Qty",anchor=CENTER)
        self.my_tree.heading("Sale Type",text="Sale Type",anchor=CENTER)

        self.my_tree.tag_configure('oddrow',background='white')
        self.my_tree.tag_configure('evenrow',background='lightblue')
        self.my_tree.pack()
        self.data_frame = LabelFrame(self.marketw, text="Enter data",height=200)
        self.data_frame.place(x=680,y=452)

        self.ID_label = Label(self.data_frame, text= "Item ID")
        self.ID_label.grid(row=0,column=0,padx=10,pady=10)
        self.ID_entry = Entry(self.data_frame)
        self.ID_entry.grid(row=0,column=1,padx=10,pady=10)

        self.ItemName_label = Label(self.data_frame, text= "Item Name")
        self.ItemName_label.grid(row=0,column=2,padx=10,pady=10)
        self.ItemName_entry = Entry(self.data_frame)
        self.ItemName_entry.grid(row=0,column=3,padx=10,pady=10)

        self.UnitPrice_label = Label(self.data_frame, text= "Unit Price")
        self.UnitPrice_label.grid(row=0,column=4,padx=10,pady=10)
        self.UnitPrice_entry = Entry(self.data_frame)
        self.UnitPrice_entry.grid(row=0,column=5,padx=10,pady=10) 

        self.ItemType_label = Label(self.data_frame, text= "Item Type")
        self.ItemType_label.grid(row=1,column=0,padx=10,pady=10)
        self.ItemType_entry = Entry(self.data_frame)
        self.ItemType_entry.grid(row=1,column=1,padx=10,pady=10)

        self.ItemQty_label = Label(self.data_frame, text= "Item Quantity")
        self.ItemQty_label.grid(row=1,column=2,padx=10,pady=10)
        self.ItemQty_entry = Entry(self.data_frame)
        self.ItemQty_entry.grid(row=1,column=3,padx=10,pady=10)

        self.SaleType_label = Label(self.data_frame, text= "Sale Type")
        self.SaleType_label.grid(row=1,column=4,padx=10,pady=10)
        self.SaleType_entry = Entry(self.data_frame)
        self.SaleType_entry.grid(row=1,column=5,padx=10,pady=10) 
        
        self.query_data()
        self.MarketCheckBox()
        self.marketw.mainloop()

    def query_data(self):
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, "Items and products.db")
        self.base = sqlite3.connect(db)
        self.cur = self.base.cursor()
        self.tester = self.cur.execute("SELECT * FROM Items")
        self.runner = self.cur.fetchall()

        '''i=0
        for ro in self.tester:
            self.my_tree.insert(parents='',index='end', text='', values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))
            i = i + 1'''
        
        global count
        count = 0

        for record in self.runner:
            if count % 2==0:
                self.my_tree.insert(parent='',index='end',iid=count,values=(record),tags=('oddrow', ))
            else:
                self.my_tree.insert(parent='',index='end',iid=count,values=(record),tags=('evenrow', ))
            count+=1
        
        self.my_tree.pack()
        self.base.commit()
        self.base.close()

    def select_record(self):
        
        self.ID_entry.delete(0, END)
        self.ItemName_entry.delete(0, END)
        self.UnitPrice_entry.delete(0, END)
        self.ItemType_entry.delete(0, END)
        self.ItemQty_entry.delete(0, END)
        self.SaleType_entry.delete(0, END)

        self.selected = self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')

        self.ID_entry.insert(0, self.values[0])
        self.ItemName_entry.insert(0, self.values[1])
        self.UnitPrice_entry.insert(0, self.values[2])
        self.ItemType_entry.insert(0, self.values[3])
        self.ItemQty_entry.insert(0, self.values[4])
        self.SaleType_entry.insert(0, self.values[5])

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
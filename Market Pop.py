import imp
from msilib.schema import Class
import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class MarketPop:

    def __init__(self):
        self.marketpopw = Tk()
        self.marketpopw.title("Query Pop out")
        Height
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:13:09 2020

@author: Dekker
"""

from tkinter import *
import os
import sys


window=Tk()
window.title("OBS")
window.geometry('550x200')

def run():
    os.system('scryfall.py')

L1 = Label(window, text="Cart Name").place(x = 25, y = 15)
E2 = Entry(window,).place(x = 100, y = 15)
B = Button(window, text ="Click Me!",command=run).place(x = 230, y = 11)




window.mainloop()
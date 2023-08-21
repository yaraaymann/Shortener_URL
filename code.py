from cgitb import text
from tkinter import font
import pyshorteners
import tkinter as tk
from tkinter import *


def shorten_it():
    #get the long URL
    old = long_link.get()
    #create the shortened URL
    short = pyshorteners.Shortener().tinyurl.short(old)
    
    newtext = StringVar()
    newtext.set(short)
    new = tk.Label(window, text='Shortened URL', bg='white', fg='brown', font='Arial 16 bold').place(x=20,y=220)
    #to show the new URL
    new_get = tk.Entry(window, bd=0 ,fg='brown' ,width=27,textvariable=newtext , font='Arial 17 bold').place(x=210,y=220)
    
    print(short)
    
#create a window  
window = tk.Tk(className='Shorten URL')
window.geometry('600x320')
window.configure(background='lightgrey')

long_link = tk.StringVar()
old_link = tk.Label(window, text='Enter long URL', background='white', foreground='black', font='Arial 16 bold').place(x=18,y=35)
#to enter the long URL
get_old_link = tk.Entry(window, bg='white', fg='black' , textvariable=long_link , width=30, justify='left' , font='Arial 17 bold').place(x=200,y=35)

short_Button = tk.Button(window, text='Shorten URL', bg='brown', fg='white', font='Arial 17 bold', command=shorten_it).place(x=200,y=110)


window.mainloop()

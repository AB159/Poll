'''
Poll v 3.0
By Alex 5/1=4/2018
'''
from tkinter import *
import ast
root = Tk()
root.title("Poll v3")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="How many siblings?").grid(row=1,column=0)

textbox1 = Entry(root)
textbox2 = Entry(root)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)

btn1 = Button(root, text= "Submit", command=root.destroy)
btn1.grid(row=2,column=0)
btn2 = Button(root, text= "Average", command=root.destroy)
btn2.grid(row=2,column=1)
btn3 = Button(root, text= "Quit", command=root.destroy)
btn3.grid(row=2,column=2)


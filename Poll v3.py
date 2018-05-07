'''
Poll v 3.0
By Alex 5//4/2018
'''
from tkinter import *
import ast
names = {}
try:    
    file = open("file.txt", "r")
    names = file.read()
    names = ast.literal_eval(names)
    file.close()
except:
    names = {}

def submitInput():
    name = textbox1.get()
    number = textbox2.get()
    if name ==  "":
        messagebox.showerror("Box Title","Name can't be blank")
        return
    if name in names:
        messagebox.showerror("Box Title","Name already used")
        return
    try:
        number = float(number)
    except:
         messagebox.showerror("Box Title","Please enter a number")
         return
    if number < 0:
        messagebox.showerror("Box Title","Number must be 0 or greater")
        return
    names[name] = number
    messagebox.showinfo("Names", names)
    textbox1.delete(0,END)
    textbox2.delete(0,END)
    file = open("file.txt", "w")
    file.write(str(names))
    file.close()
    
root = Tk()
root.title("Poll v3")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="How many siblings?").grid(row=1,column=0)

textbox1 = Entry(root)
textbox2 = Entry(root)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
def calAverage():
    messagebox.showinfo("Title",str(len(names)) +" Responses ")
    if len(names) > 0:
        messagebox.showinfo(" Average", sum(names.values())/len(names))

btn1 = Button(root, text= "Submit", command=submitInput)
btn1.grid(row=2,column=0)
btn2 = Button(root, text= "Average", command=calAverage)
btn2.grid(row=2,column=1)
btn3 = Button(root, text= "Quit", command=root.destroy)
btn3.grid(row=2,column=2)



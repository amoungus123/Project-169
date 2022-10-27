# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:08:08 2022

@author: pulle
"""

from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("GUI Creator")
root.configure(bg="lavender")

class CreateButton:
    
    def __init__(self):
        print("This is a CreateElements Class")
        
    def createNewButton(self):
        btn = Button(root, text = "Button", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
class CreateLabel:
    
    def __init__(self):
        print("This is a CreateElements Class")
        
    def createNewLabel(self):
        label = Label(root,text ="A new label has been created using Class", fg="red")
        label.pack()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")

obj_of_CreateButton = CreateButton()

btn = Button(root, text ="Click to create Button element", command = obj_of_CreateButton.createNewButton)
btn.pack(padx=20, pady = 10)

obj_of_CreateLabel = CreateLabel()

btn = Button(root, text ="Click to create label element", command = obj_of_CreateLabel.createNewLabel)
btn.pack(padx=20, pady = 10)


root.mainloop()
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar, Progressbar
from tkinter import ttk 
from PIL import Image,ImageTk 
import mysql.connector 
import cv2
import os
import numpy as np 



class Developer: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x800+0+0")  
        self.root.title("Face Recognition System") 

        
     # Background Image 

        bg_img = Image.open(r"photos\background.png")  
        bg_img = bg_img.resize((1530,800),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(bg_img)   

        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=0) 

        # Heading text 

        title_lbl = Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="dark blue",fg="white") 
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Yash Pic 

        img = Image.open(r"photos\yash.jpg") 
        img = img.resize((200,200),Image.ANTIALIAS) 
        self.photoimg=ImageTk.PhotoImage(img)  
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=50,y=200)


        # Description of Yash Image 

        title_lbl = Label(bg_img, text = "I welcome you are all to Our Software. ", font=("times new roman",30,"bold"))
        title_lbl.place(x=310,y=200)  

        b1_1 = Label(bg_img,text="Yash Kumar Sharma",font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=47, y=400, width = 205, height = 35)   



root = Tk()
my_gui = Developer(root)   
root.mainloop()



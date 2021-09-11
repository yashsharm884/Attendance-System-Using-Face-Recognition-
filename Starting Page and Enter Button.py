from tkinter import*
import tkinter
from tkinter import ttk 
from PIL import Image,ImageTk 

class MyFirstGUI:
    def __init__(self, root):
        self.root = root
        root.title("A simple GUI")
        root.geometry("1900x800+0+0")  
        root.title("Face Recognition System")    
        
        # First Image

        img = Image.open(r"D:\JECRC\2nd Semester\Minor Project\My_Final_Work\header1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS) 
        self.photoimg=ImageTk.PhotoImage(img)  
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)

        # Second Image

        img1 = Image.open(r"D:\JECRC\2nd Semester\Minor Project\My_Final_Work\header2.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS) 
        self.photoimg1=ImageTk.PhotoImage(img1)   
        f_lbl = Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=500,y=0)

        # Third Image

        img2 = Image.open(r"D:\JECRC\2nd Semester\Minor Project\My_Final_Work\header3.jpg")  
        img2 = img2.resize((550,130),Image.ANTIALIAS) 
        self.photoimg2=ImageTk.PhotoImage(img2)   
        f_lbl = Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=1000,y=0)

        # Background Image 

        img3 = Image.open(r"D:\JECRC\2nd Semester\Minor Project\My_Final_Work\background.jpg")  
        img3 = img3.resize((1530,710),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=130) 

        # Heading Text 

        title_lbl = Label(bg_img, text = "Face Recognition System", font=("times new roman",30,"bold"),fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Student Button

        img4 = Image.open(r"D:\JECRC\2nd Semester\Minor Project\My_Final_Work\background.jpg")  
        img4 = img4.resize((220,220),Image.ANTIALIAS)   
        self.photoimg4=ImageTk.PhotoImage(img4)  

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")  
        b1.place(x=200,y=100,width=220,height=220)







        
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


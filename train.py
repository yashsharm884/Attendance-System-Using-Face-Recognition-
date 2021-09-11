from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar, Progressbar
from tkinter import ttk 
from PIL import Image,ImageTk 
import mysql.connector 
import cv2
import os
import numpy as np 


class Train: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x800+0+0")  
        self.root.title("Face Recognition System") 

        # Background Image 

        bg_img = Image.open(r"photos\background2.png")  
        bg_img = bg_img.resize((1530,800),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(bg_img)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=0) 

        # Heading text 

        title_lbl = Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="dark blue",fg="white") 
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Middle Image

        img = Image.open(r"photos\train_mid.jpg")
        img = img.resize((500,270),Image.ANTIALIAS) 
        self.photoimg=ImageTk.PhotoImage(img)  
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=130) 

        # Button

        mid_lbl = Button(self.root,text="Start Training",command=self.train_classifier,font=("times new roman",35,"bold"),bg="dark blue",fg="white") 
        mid_lbl.place(x=500,y=450,width=520,height=45)  

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir) ] 


        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')   # Gray Scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)

            cv2.waitKey(1)==13    # enter 
        ids=np.array(ids)


        # Train the Classifier and Save it. 

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Successful")













        






 





root = Tk()
my_gui = Train(root) 
root.mainloop()

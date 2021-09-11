from tkinter import*
import tkinter
from tkinter import ttk 
from PIL import Image,ImageTk   # Operations on Image. 
import os

class face_recognition123:               
    def __init__(self, root):            # root is the name of the windows. 
        self.root = root                   # Initializing the Root. 
        root.geometry("1900x800+0+0")  
        root.title("Face Recognition System")    
        
        # First Image

        img = Image.open(r"photos\header1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)  # ANTIALIAS convert high level image  to low level image.
        self.photoimg=ImageTk.PhotoImage(img)  
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)

        # Second Image

        img1 = Image.open(r"photos\header2.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS) 
        self.photoimg1=ImageTk.PhotoImage(img1)   

        f_lbl = Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=500,y=0)

        # Third Image

        img2 = Image.open(r"photos\header3.jpg")  
        img2 = img2.resize((550,130),Image.ANTIALIAS) 
        self.photoimg2=ImageTk.PhotoImage(img2)   
        
        f_lbl = Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=1000,y=0)

        # Background Image 

        img3 = Image.open(r"photos\background.jpg")  
        img3 = img3.resize((1530,710),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=130) 

        # Heading Text 

        title_lbl = Label(bg_img, text = "Face Recognition System", font=("times new roman",30,"bold"),bg="lawn green",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Student Button

        img4 = Image.open(r"photos\face_recognizer.png")  
        img4 = img4.resize((220,220),Image.ANTIALIAS)   
        self.photoimg4=ImageTk.PhotoImage(img4)  

        # command=self.student_details,

        b1 = Button(bg_img, image=self.photoimg4,command=student_details, cursor="hand2")  
        b1.place(x=50,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=student_details,  cursor="hand2", font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=50,y=300,width=220,height=40)


        #  Detect Face Button

        img5 = Image.open(r"photos\face_detector.png")  
        img5 = img5.resize((220,220),Image.ANTIALIAS)   
        self.photoimg5=ImageTk.PhotoImage(img5)   

        b1 = Button(bg_img, image=self.photoimg5, command=face_recognize,cursor="hand2")  
        b1.place(x=300,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",command=face_recognize, cursor="hand2", font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=300,y=300,width=220,height=40) 

        #  Attendance 

        img6 = Image.open(r"photos\Attendance.jpg") 
        img6 = img6.resize((220,220),Image.ANTIALIAS)   
        self.photoimg6=ImageTk.PhotoImage(img6)   

        b1 = Button(bg_img, image=self.photoimg6,command=Attendance, cursor="hand2")  
        b1.place(x=550,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Attendance", cursor="hand2",command=Attendance, font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=550,y=300,width=220,height=40) 
 
        # Train Data 

        img7 = Image.open(r"photos\Train.jpg")  
        img7 = img7.resize((220,220),Image.ANTIALIAS)   
        self.photoimg7=ImageTk.PhotoImage(img7) 

        b1 = Button(bg_img, image=self.photoimg7,command=train_data, cursor="hand2")  
        b1.place(x=50,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Train Data", cursor="hand2",command=train_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=50,y=580,width=220,height=40) 

        # Photos 

        img8 = Image.open(r"photos\photosample.png")  
        img8 = img8.resize((220,220),Image.ANTIALIAS)   
        self.photoimg8=ImageTk.PhotoImage(img8)   

        b1 = Button(bg_img, image=self.photoimg8,command=self.open_img, cursor="hand2")  
        b1.place(x=300,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos", cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=300,y=580,width=220,height=40) 
        
        # Developer Section 

        img9 = Image.open(r"photos\Developer.jpeg")  
        img9 = img9.resize((220,220),Image.ANTIALIAS)   
        self.photoimg9=ImageTk.PhotoImage(img9)   

        b1 = Button(bg_img, image=self.photoimg9,command=developer_section, cursor="hand2")    
        b1.place(x=550,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Developer", cursor="hand2",command=developer_section, font=("times new roman",15,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=550,y=580,width=220,height=40) 

    def open_img(self):
        os.startfile("data") 




def student_details():    
    print("Student Management Page Opened") 
    root.withdraw()  
    os.system("python student.py") 
    root.state('zoomed')
    root.deiconify()
    return

def train_data():      
    print("Training Data Opened")   
    root.withdraw()  
    os.system("python train.py")  
    root.state('zoomed')
    root.deiconify()
    return


def face_recognize():      
    print("Face Recognize Opened")     
    root.withdraw()  
    os.system("python face_recognition.py")  
    root.state('zoomed')
    root.deiconify()
    return

def developer_section():     
    print("Developer Section Opened ") 
    root.withdraw()  
    os.system("python developer.py")  
    root.state('zoomed')
    root.deiconify()
    return



def Attendance():     
    print("Attendance Section Opened ") 
    root.withdraw()  
    os.system("python attendance.py")  
    root.state('zoomed')
    root.deiconify()
    return

    






        


















        
root = Tk()
my_gui = face_recognition123(root)    # my_gui is the object of the class. 
root.mainloop()


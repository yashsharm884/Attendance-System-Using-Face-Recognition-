from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar, Progressbar
from tkinter import ttk 
from PIL import Image,ImageTk 
import mysql.connector 
import cv2
import os
import numpy as np 
from datetime import datetime
from time import strftime


class Face_recognition: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x800+0+0")  
        self.root.title("Face Recognition System") 
    

     # Background Image 

        bg_img = Image.open(r"photos\face_detect.jpg")  
        bg_img = bg_img.resize((1530,800),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(bg_img)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=0) 

        # Heading text 

        title_lbl = Label(self.root,text="Face Detector",font=("times new roman",35,"bold"),bg="dark blue",fg="white") 
        title_lbl.place(x=0,y=0,width=1530,height=45)  


        # Face Detector 

        b1_1 = Button(self.root,text="Face Recognition",command=self.face_recog,font=("times new roman",35,"bold"),bg="green",fg="white") 
        b1_1.place(x=500,y=710,width=520,height=45)   

    def mark_attendance(self,s,r,n):   
        with open("attendance.csv","r+",newline="\n") as f: 
            myDataList = f.readlines()
            name_list = []
            for line in myDataList: 
                entry = line.split((","))
                name_list.append(entry[0])
            if( (s not in name_list) and (r not in name_list) and (n not in name_list) ): 
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{dtString},{d1},Present")  


















        # Face Recognition 

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor, minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predit=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100 * (1-predit/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()

                id = str(id) 

                my_cursor.execute("select student_id from student where student_id=" + id ) 
                n=my_cursor.fetchone()
                #n = str(n) 
                n="".join(n)

                my_cursor.execute("select Roll from student where student_id=" + str(id) )    
                r=my_cursor.fetchone()
                #r = str(r) 
                r="".join(r) 

                my_cursor.execute("select Name from student where student_id=" + str(id))
                s=my_cursor.fetchone()
                s="".join(s)   


                if confidence > 75:
                    cv2.putText(img,f"Name:{s}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  
                    cv2.putText(img,f"Roll_Number:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                    cv2.putText(img,f"Studentid_is:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(s,r,n)  

                else:
                    print("Not Face") 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face:",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]     
            return coord


        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf) 
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:   # Enter Key 
                break
        video_cap.release()
        cv2.destroyAllWindows()

root = Tk()
my_gui = Face_recognition(root) 
root.mainloop()



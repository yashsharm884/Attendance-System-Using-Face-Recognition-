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
import csv
from tkinter import filedialog  
from email import message
import os
import smtplib as s
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders










mydata=[]
class Attendance: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x800+0+0")  
        self.root.title("Face Recognition System") 

        # Variables 

        self.var_name=StringVar() 
        self.var_roll=StringVar()
        self.var_id=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()  
        self.var_attendance=StringVar()  
        
        # Background Image 

        img3 = Image.open(r"photos\background3.png")  
        img3 = img3.resize((1530,710),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=0) 

        # Heading Text 

        title_lbl = Label(bg_img, text = "Attendance System",bg="green",fg="yellow",padx = 15, pady = 15, font = ("Times New Roman", 20, "bold") ,borderwidth = 15)
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Frame 

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=155,width=1550,height=650) 

        # Left Label Frame 

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Attendance Details",font=("times new roman",12,"bold")) 
        Left_frame.place(x=10,y=10,width=760,height=580)

        # Left Frame Image 

        img_left = Image.open(r"photos\left_frame.jpg")  
        img_left = img_left.resize((740,150),Image.ANTIALIAS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)   

        f_lbl = Label(Left_frame,image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=740,height=150)   

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE, text="Student Information",font=("times new roman",12,"bold")) 
        class_Student_frame.place(x=5,y=150,width=740,height=300) 

        # ID 
        
        dep_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)  

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_id, font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         # Name 

        semester_label=Label(class_Student_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=0,column=2,padx=10,sticky=W)  

        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         # Roll Number 

        roll_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,sticky=W)  

        
        roll_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W) 

        # Name,Roll No.,ID,Time,Date,Attendance

        # Date 

        roll_label=Label(class_Student_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,sticky=W)  

        
        roll_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W) 

        # Time 

        roll_label=Label(class_Student_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=2,column=0,padx=10,sticky=W)  

        
        roll_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        roll_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W) 

        # Attendance 

        roll_label=Label(class_Student_frame,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=2,column=2,padx=10,sticky=W)  

        
        roll_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_attendance,font=("times new roman",13,"bold"))
        roll_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W) 

        # Buttons 
        
        btn_frame = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white" )   # bd means border and RELIEF means style of widget. 
        btn_frame.place(x=0,y=170,width=715,height=80)  

        save_btn = Button(btn_frame,text="Import CSV", width=17,command=self.importCsv, font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row= 0, column= 0) 
        
        update_btn = Button(btn_frame,text="Export CSV", width=17,command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row= 0, column= 1)  

        
        delete_btn = Button(btn_frame,text="Update", command=self.action, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row= 0, column= 2)  

        
        reset_btn = Button(btn_frame,text="Reset", width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row= 0, column= 3)    
        
        # Send Mail Button 
        
        send_mail_btn = Button(btn_frame,text="Send Mail",command=self.Send_mail, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        send_mail_btn.grid(row= 1, column= 1)     

        

        





        # Right Label Frame 

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))  
        Right_frame.place(x=780,y=10,width=720,height=600)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455) 

        # ================== Scroll Bar =========================

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL) 

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","Name","Roll_No","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   

        
        scroll_x.pack(side=BOTTOM,fill=X)    
        scroll_y.pack(side=RIGHT,fill=Y)  


        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.xview)    

        
        
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Roll_No",text="Roll_No") 
        self.AttendanceReportTable.heading("id",text="id")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date") 
        self.AttendanceReportTable.heading("Attendance",text="Attendance")   


        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)    
        
        
        # Fetch Data
        
    def fetchData(self,rows): 
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children() )
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i) 

    # Import CSV File 

    def importCsv(self):
        global mydata 
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)  
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")  
            for i in csvread: 
                mydata.append(i) 
            self.fetchData(mydata) 


    # Export CSV File 

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root) 
                return False; 
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",") 
                for i in mydata: 
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es: 
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  
    
     # Cursor Function 

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row) 
        rows = content['values']
        self.var_name.set(rows[0]) 
        self.var_roll.set(rows[1]) 
        self.var_id.set(rows[2]) 
        self.var_time.set(rows[3]) 
        self.var_date.set(rows[4]) 
        self.var_attendance.set(rows[5]) 

    # Reset Data 

    def  reset_data(self):

        self.var_name.set("")
        self.var_roll.set("")  
        self.var_id.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("") 


    # Update Data 

    def action(self):

        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row) 
        rows = content['values'] 
        
        
        id = self.var_name.set(rows[0]) 
        roll = self.var_roll.set(rows[1]) 
        name = self.var_id.set(rows[2]) 
        time = self.var_time.set(rows[3]) 
        date = self.var_date.set(rows[4]) 
        attendn = self.var_attendance.set(rows[5]) 
        
        # write to csv file
        try:
            Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer= csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Name":name,
                "Roll":roll,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def Send_mail(self):

        try:
            ob = s.SMTP("smtp.gmail.com",587) 
            ob.starttls()
            ob.login("yashsharm884@gmail.com","dbmsnormalforms123456")
            subject = "Sending Email Using Python"
            body = "Testing Mail"
            message = "Subject: {}\n\n{}".format(subject,body)
            filename = "attendance.csv"
            attachment = open("attendance.csv", "rb") 
            msg = MIMEMultipart()
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            text = msg.as_string()
            listOfAddress = ["yash.20mcin005@jecrcu.edu.in"]
            ob.sendmail("yashsharm884@gmail.com",listOfAddress,text)  
            print(message) 

            messagebox.showinfo("Sending Mail","Mail Successful",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    






    

        

        






root = Tk()
my_gui = Attendance(root) 
root.mainloop()


from tkinter import*
from tkinter import messagebox
from tkinter import ttk 
from PIL import Image,ImageTk 
import mysql.connector 
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        root.geometry("1900x800+0+0")  
        root.title("Face Recognition System") 

        # Variables 

        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar() 
        self.var_address=StringVar()
        


        # Background Image 

        img3 = Image.open(r"photos\background3.png")  
        img3 = img3.resize((1530,710),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=0) 

        # Heading Text 

        title_lbl = Label(bg_img, text = "Student Management System",bg="green",fg="yellow",padx = 15, pady = 15, font = ("Times New Roman", 20, "bold") ,borderwidth = 15)
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        # Frame 

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=155,width=1550,height=650) 

        # Left Label Frame 

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold")) 
        Left_frame.place(x=10,y=10,width=760,height=580)

        # Left Frame Image 

        img_left = Image.open(r"photos\left_frame.jpg")  
        img_left = img_left.resize((740,150),Image.ANTIALIAS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)   

        f_lbl = Label(Left_frame,image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=740,height=150)   


        # department == course 

        # Current Course Label Frame 

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE, text="Current Course Information",font=("times new roman",12,"bold")) 
        current_course_frame.place(x=5,y=160,width=740,height=80) 

        dep_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)  

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")  
        dep_combo["values"]=("Select Course","BCA","MCA","B.Tech","M.Tech")   
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)  
 
        
        # Semester 

        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=0,column=2,padx=10,sticky=W)  

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")  
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")  
        semester_combo.current(0)
        semester_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)    # padx and pady means gap from x and y axis.

        # sticky means if cell is large than widget then it can maintain it.  


        # Class Student Information 

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE, text="Student Information",font=("times new roman",12,"bold")) 
        class_Student_frame.place(x=5,y=250,width=740,height=300) 

        # Student id

        studentID_label = Label(class_Student_frame,text="Roll No.:",font=("times new roman",13,"bold"), bg = "white" ) 
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)   

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name 

        
        studenName_label = Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"), bg = "white" ) 
        studenName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)   

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Gender  
        
        gender_label = Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"), bg = "white" ) 
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)   

        # gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)  

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")  
        gender_combo["values"]=("Male","Female","Other")    
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)     


        
        # Email
        
        email_label = Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"), bg = "white" ) 
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)   

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)  

        # Phone No. 
        
        phone_label = Label(class_Student_frame,text="Mobile:",font=("times new roman",13,"bold"), bg = "white" ) 
        phone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)   

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_mobile,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)   

        # Address 
        
        address_label = Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"), bg = "white" ) 
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)   

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)      



        # Radio Button 
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample",value="Yes") 
        radiobtn1.grid(row=7,column=0)

        self.var_radio2=StringVar()
        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample",value="N")  
        radiobtn2.grid(row=7,column=1)

        # Buttons Frame 

        btn_frame = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white" )   # bd means border and RELIEF means style of widget. 
        btn_frame.place(x=0,y=170,width=715,height=30)   



        save_btn = Button(btn_frame,text="Save",command=self.add_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row= 0, column= 0) 
        
        update_btn = Button(btn_frame,text="Update",command=self.update_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row= 0, column= 1)  

        
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row= 0, column= 2)  

        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,  width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row= 0, column= 3)    

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=715,height=31)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white" )
        take_photo_btn.grid(row= 1, column= 0)

        update_btn = Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset, width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row= 1, column= 1)   

        # Right Label Frame 

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold")) 
        Right_frame.place(x=790,y=10,width=720,height=580)

        
        # Right Frame Image   

        img_right = Image.open(r"photos\right_frame.png")  
        img_right = img_right.resize((740,150),Image.ANTIALIAS)  
        self.photoimg_right=ImageTk.PhotoImage(img_right)   

        f_lbl = Label(Right_frame,image=self.photoimg_right) 
        f_lbl.place(x=5,y=0,width=740,height=150)  

        # Search System

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold")) 
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white") 
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)   

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=14)  
        search_combo["values"]=("Select", "Roll_No","Phone_no","Email")  
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        search_entry=ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(Search_frame,text="Search", width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row= 0, column= 3)    

        showAll_btn = Button(Search_frame,text="Show All", width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row= 0, column= 4)   

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=300) 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)  
   
        self.student_table=ttk.Treeview(table_frame,columns=("Course","Semester","Name","Roll_No","Mobile","Email","Address","Gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set ) 

        # Treeview widget holds a list of items.




        scroll_x.pack(side=BOTTOM,fill=X)    
        scroll_y.pack(side=RIGHT,fill=Y)  


        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)   

        

        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Roll_No",text="Roll_No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Mobile",text="Mobile")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)  
        self.fetch_data()




    def add_data(self):
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_radio1.get() 

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Added",parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)} ", parent=self.root)     

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children() )
            for i in data:
                self.student_table.insert("",END,values=i) 
            conn.commit()
        conn.close()


    def get_cursor(self,event):  
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_semester.set(data[1]),
        self.var_name.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_mobile.set(data[4]),
        self.var_email.set(data[5]),
        self.var_address.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_radio1.set(data[8])

 

    def update_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root) 
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)

                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set course=%s,semester=%s,Name=%s,Mobile=%s,Email=%s,Address=%s,Gender=%s,PhotoSample=%s where Roll=%s", ( 

                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.var_radio1.get(), 
                        self.var_roll.get()       ))   

                else:

                    if not Update:
                        return
                messagebox.showinfo("Success","Record Updated",parent=self.root)  

                 # parent means actions are on that particular windwo only. 
                    
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)} ",parent=self.root)              

    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll No Must Needed",parent=self.root)
        else:
            try:

                delete=messagebox.askyesno("Student Delete","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Roll=%s"
                    val=(self.var_roll.get(), )
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

    def reset_data(self):
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_gender.set("")
        self.var_radio1.set("")  


    def generate_dataset(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set course=%s,semester=%s,Name=%s,Mobile=%s,Email=%s,Address=%s,Gender=%s,PhotoSample=%s where Roll=%s", ( 

                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_radio1.get(), 
                                                                                                                                                                self.var_roll.get()       
                ))   

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)  # Scaling factor = 1.3 and Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                
                while True:  
                    ret,my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)

                       # cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

                        cv2.imshow("Cropped Face",face) 

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Datasets Completed") 

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 



            





root = Tk()
my_gui = Student(root)
root.mainloop()
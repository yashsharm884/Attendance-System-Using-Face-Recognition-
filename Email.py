wfrom email import message
import os
import smtplib as s
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders















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




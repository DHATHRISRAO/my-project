#! /usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com' ,587)
s.starttls()
s.login("dhathrirao@gmail.com" ,"26636242")
message ="hiiiiiii"
s.sendmail("dhathrirao@gmail.com","dhathrirao@gmail.com",message)
s.quit()
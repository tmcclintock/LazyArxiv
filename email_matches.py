import smtplib
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from datetime import datetime
#import os, sys

def initialize_email_server():
    usr='calvin.job.done'
    psw='hobbesrules!'
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usr,psw)
    return server

def send_email(server, fromaddr, toaddr, body):
    msg = MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']="Yesterday's Interesting Arxiv Papers"
    msg.attach(MIMEText(body))

    # Send the email
    server.sendmail(fromaddr, toaddr, msg.as_string())
    return    

def shutdown_email_server(server):
    server.quit()
    return

#def noticeEMail(usr, psw, fromaddr, toaddr, body):
#	"""
#	Sends an email message through GMail once the script is completed.  
#	Developed to be used with AWS so that instances can be terminated 
#	once a long job is done. Only works for those with GMail accounts.
#
#	starttime : a datetime() object for when to start run time clock
#
#	usr : the GMail username, as a string
#
#	psw : the GMail password, as a string 
#
#	fromaddr : the email address the message will be from, as a string
#
#	toaddr : a email address, or a list of addresses, to send the 
#			 message to
#	"""
#
#	# Initialize SMTP server
#	server=smtplib.SMTP('smtp.gmail.com:587')
#	server.starttls()
#	server.login(usr,psw)
#
#	# Prepare email object
#	subject="Yesterday's Interesting Arxiv Papers"
#	msg = MIMEMultipart()
#	msg['From']=fromaddr
#	msg['To']=toaddr
#	msg['Subject']=subject
#	msg.attach(MIMEText(body))
#
#    # Send the email
#	server.sendmail(fromaddr, toaddr, msg.as_string())
#	server.quit()


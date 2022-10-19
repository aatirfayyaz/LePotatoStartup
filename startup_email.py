import subprocess
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#Account Information
####################

to = 'YOUREMAIL@gmail.com'
gmail_user = 'SENDEREMAIL@gmail.com'
gmail_password = 'PASSWORDFROMAPP'
host = 'smtp.gmail.com'
port = 465

###################

now = datetime.now()

p = os.popen("ifconfig | grep 'inet '").read()

print("***********************")
print("Current IPs = ")
print(p)
print("END IPs")
print("***********************")

subject = 'IP Address for Le Potato AML-S905X-CC on %s' %now.strftime('%m/%d/%Y, %H:%M:%S')
content_text = 'IP Addresses:' + str(p)

message = MIMEMultipart()
message['From'] = Header(gmail_user)
message['To'] = Header(to)
message['Subject'] = Header(subject)
message.attach(MIMEText(content_text, 'plain', 'utf-8'))

server = smtplib.SMTP_SSL(host, port)
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, to, message.as_string())
server.quit()

print('Mail Sent Successfully!')
print("***********************")

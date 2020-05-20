## this program won't run here,you need to copy it in your local system and then enter your valid credentials,also you will have to turn allow unsecure connection in your google account ON for once(since we are requesting an INGRESS connection),I recommend turning it OFF once you are done with this!

#Enough of the instructions,now go enjoy the source code and give it a try!

#importing the smtp(simple mail transfer protocol) built in module,we will need it to create our local smtp server
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

email=EmailMessage() #creating email object

email['from']='   ' #Enter source mail here in the string
email['to']='   ' #Enter destination mail here

email['subject']='Gaurav Gaur' #enter a subject of your choice

email.set_content("Hello,this is a custom generated email from my new python project which generates custom email and sends it to the users,thanks for being a part of it!") #enter the content of the mail

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp: #setting up our smtp server
	smtp.ehlo()
	smtp.starttls()
	smtp.login('mail_id ','mail_pwd') #enter your mail id and password in 1st and 2nd parameter
	smtp.send_message(email)
	print('all good')

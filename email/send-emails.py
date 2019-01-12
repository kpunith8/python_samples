# Sending emails using 'smtplib' library
# require a smtp server info of an email provider, for gmail: smtp.gmail.com
# It requires app password to authenticate with smtp server

import smtplib
import getpass

# try 465 as port number if 587 does not work or pass nothing to port number
# firewall may block the connection to SMTP server, make sure firewall is diabled
# or exclusion added to the firewall rules

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
# To check whether connection established call 'ehlo()' on 'smtp_object',
# it should be the next line after creting SMTP connection
smtp_object.ehlo()

# port 587 needs to call 'starttls()' on 'smtp_object' to use TLS protocol
# if the server conneted to 465, it used SSL, which doesnot require 'starttls()' to be called on 'smtp_object'
smtp_object.starttls()

# To login to gmail and establish 2 step verification, signin using app passwords and select 2-step verification
# once the Application password generated, store the pass in some file
email = input("Enter your Email:")
# Ask password in the command line and hide is using 'getpass' built-in module,
# instead of saving and reading from a variable
password = getpass.getpass("Enter your password:")

# Password should be app password not the actual one
smtp_object.login(email, password)

# Send an mail
from_address = email
to_address = email
subject = input("Enter the subject:")
message = input("Enter the message body:")
full_email = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address, to_address, full_email)

# Close the connection
smtp_object.quit()

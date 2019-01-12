# To view recieved e-mail use built-in libraries 'imaplib' and 'email' libraries
import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL("imap.gmail.com")

email_id = input("Enter your Email:")
password = getpass.getpass("Enter your password:")

M.login(email_id, password)

# To list the available inbox
# M.list()

M.select("inbox")

# data will have mail information
typ, data = M.search(None, "BEFORE 01-Nov-2018")
# some examples using search patterns
# FROM user@abc.com
# SUBJECT "new test"

email_id_1 = data[0]

# email_data consists of subject and message and other info
result, email_data = M.fetch(email_id_1, "(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

# parse the 'raw_email_string' using 'email' library
email_message = email.message_from_string(raw_email)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print("Message body:", body)

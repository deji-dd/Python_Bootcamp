import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')
emails = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
M.login(emails, password)
M.select('inbox')
typ, data = M.search(None, 'SUBJECT "Python Test"')
print(typ)
id1 = data[0]
result, email_data = M.fetch(id1, '(RFC822)')
raw_email = email_data[0][1]
str_email = raw_email.decode('utf-8')
email_message = email.message_from_string(str_email)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)

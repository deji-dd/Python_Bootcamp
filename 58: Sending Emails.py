import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
email = getpass.getpass('Your E-mail: ')
password = getpass.getpass('Your password: ')
smtp_object.login(email, password)
from_address = email
to_address = getpass.getpass("Recipient Email: ")
subject = input('Enter the subject: ')
body = input('Enter body message: ')
msg = f"Subject: {subject}\n{body}"
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()

import os
import smtplib
from email.message import EmailMessage

dante_email = os.environ.get('dante_gmail')
dante_password = os.environ.get('dante_gmail_password')

body = 'I hope you are having a good day :)'

msg = EmailMessage()
msg['Subject'] = 'Hi Tia'
msg['From'] = dante_email
msg['To'] = 'tnuzzolilli@gmail.com'
msg.set_content(body)

def gab_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(dante_email, dante_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    gab_email()
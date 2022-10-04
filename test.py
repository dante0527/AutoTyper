import os
import smtplib
from email.message import EmailMessage

sender_email = os.environ.get('dante_gmail')
sender_password = os.environ.get('dante_gmail_password')

body = 'I hope you are having a good day :)'

msg = EmailMessage()
msg['Subject'] = 'Hi Buddy'
msg['From'] = sender_email
msg['To'] = 'testemail123@gmail.com'
msg.set_content(body)

def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email()

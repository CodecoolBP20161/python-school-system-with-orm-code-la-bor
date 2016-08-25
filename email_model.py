import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *
import json


class EmailSender:

    with open("login.json") as login:
        login_data = json.load(login)

    user = login_data["user"]
    password = login_data["password"]

    @classmethod
    def email_send(cls, to_address, body, subject):
        message = MIMEMultipart()
        message['From'] = cls.user
        message['To'] = to_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(cls.user, cls.password)
            server.sendmail(cls.user, to_address, message.as_string())
            print("Email sent")
            server.quit()

        except:
            print("Sending failed!")

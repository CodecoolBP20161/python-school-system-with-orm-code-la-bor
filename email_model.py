import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *


class EmailSender:

    fromaddr = "codelabor1@gmail.com"
    toaddr = 
    body = "\r\n".join([
      "Why, oh why",
      "Why, oh why",
      "Why, oh why"
      ])


    def email_send():
        try:
            fromaddr = EmailSender.fromaddr
            toaddr = EmailSender.toaddr
            msg = MIMEMultipart()
            msg['From'] = "codelabor1@gmail.com"
            msg['To'] = "lorszil@gmail.com"
            msg['Subject'] = "Welcome"
            body = EmailSender.body
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(fromaddr, "Codelabor1234")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            print("Send")
            server.quit()
        except:
            raise ("Sending failed!")

EmailSender.email_send()

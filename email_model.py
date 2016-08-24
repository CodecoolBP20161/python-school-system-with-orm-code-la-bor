import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *


fromaddr = "codelabor1@gmail.com"
toaddr = "lorszil@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Welcome"

body = "\r\n".join([
  "Why, oh why",
  "Why, oh why",
  "Why, oh why"
  ])

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, "Codelabor1234")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

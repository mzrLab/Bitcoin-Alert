import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass


def send_email():
  msg = MIMEMultipart()
  password = your_password
  msg['From'] = your_email
  msg['To'] = send_email_to
  msg['Subject'] = "Bitcoin price, ACT FAST"
  message = "Dear " + your_name + "\nBitcoin prices are now " + str(bitcoin_rate) + ". Better buy quick.\nRegards,\n" + your_name
  msg.attach(MIMEText(message, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  server.login(msg['From'], password)
  server.sendmail(msg['From'], msg['To'], message)
  
  server.quit()
  print("successfully sent email to %s:" % (msg['To']))
  print("Price of bitcoin was at " + str(bitcoin_rate))

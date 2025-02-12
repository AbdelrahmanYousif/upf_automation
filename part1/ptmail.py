import smtplib
from email.mime.text import MIMEText
import os

email = "abdorox.yousif@gmail.com"
password = os.getenv("TEST!")
print(password)
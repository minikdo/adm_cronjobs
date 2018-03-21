#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from send_email_config import *

def send_email(to_addrs, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = to_addrs
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    text = msg.as_string()
    
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    
    server.sendmail(EMAIL_FROM, to_addrs, text)
    server.quit

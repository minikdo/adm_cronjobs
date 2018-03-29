import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Send_Email():
    SMTP_HOST = os.environ['SMTP_HOST']
    SMTP_PORT = os.environ['SMTP_PORT']     
    EMAIL_FROM = os.environ['EMAIL_FROM']    
    EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
    
    def __init__(self):
        self.server = smtplib.SMTP(self.SMTP_HOST, self.SMTP_PORT)
        self.server.starttls()
        self.server.login(self.EMAIL_FROM, self.EMAIL_PASSWORD)


    def send(self, to_addrs, subject, content):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.EMAIL_FROM
        self.msg['To'] = ', '.join(to_addrs)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(content, 'plain'))
    
        content = self.msg.as_string()
        self.server.sendmail(self.EMAIL_FROM, to_addrs, content)


    def quit(self):
        self.server.quit


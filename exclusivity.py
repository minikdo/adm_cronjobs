#!/usr/bin/env python3

import sys
import os.path
from send_email import Send_Email
from string import Template
from db import DB

# import ipdb; ipdb.set_trace()

def main():

    # initialize database
    db = DB()

    # initialize send mail class
    send_email = Send_Email()
    
    # load template
    dirname = os.path.dirname(os.path.abspath(__file__))
    body_file = open(os.path.join(dirname, 'templates', 'notification.txt'), 'r')
    body_content = body_file.read()

    # get contracts close to expire 
    week_left = db.query("""select id from est where wyl > now() and 
    wyl < now() + '1 week'::interval and status=0""")

    # get expired contracts
    expired = db.query("""select id from est where wyl < now() and status=0""")

    oferty = ''
    
    for row in week_left:
        oferty += "- {} \n".format(row[0])

    body_template = Template(body_content)
    body = body_template.substitute(oferty=oferty)

    subject = 'kończące się wyłączności' 

    # get user email to notify
    emails = db.query("""select nazwa_pelna, email2 from users where aktywna='t'""")
    email_to = [email[0] + ' <' + email[1] + '>' for email in emails]

    # notify users
    send_email.send(email_to, subject, body)
    send_email.quit()
    

if __name__ == '__main__':
    main()

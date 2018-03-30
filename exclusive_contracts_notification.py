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
    
    # get contracts close to expire 
    week_left = db.query("""select id from est where wyl > now() and 
    wyl < now() + '1 week'::interval and status=0""")

    # get expired contracts
    expired = db.query("""select id from est where wyl < now() and status=0""")

    if not week_left and not expired:
        # print("brak ofert")
        exit(0)

    week_left_ids = ''
    expired_ids = ''
    
    for row in week_left:
        week_left_ids += "- {} \n".format(row[0])

    for row in expired:
        expired_ids += "- {} \n".format(row[0])
        # change contract status to suspended
        db.change_status(row[0], 4) # 4 - suspended

    # generate mail
    body = generate_mail(week_left_ids, expired_ids)

    subject = 'kończące się umowy' 

    # notify users by mail
    notify(db, subject, body)


def generate_mail(week_left_ids, expired_ids):

    # load template
    dirname = os.path.dirname(os.path.abspath(__file__))
    body_file = open(os.path.join(dirname, 'templates', 'notification.txt'), 'r')
    body_content = body_file.read()

    # substitute variables
    body_template = Template(body_content)
    body = body_template.substitute(
        week_left_ids=week_left_ids,
        expired_ids=expired_ids)

    return body


def notify(db, subject, body):

    # initialize send mail class
    send_email = Send_Email()

    # get user email to notify
    emails = db.query("""select nazwa_pelna, email2 from users where aktywna='t'""")
    email_to = [email[0] + ' <' + email[1] + '>' for email in emails]
    
    # send mail to active users
    send_email.send(email_to, subject, body)
    send_email.quit()


if __name__ == '__main__':
    main()

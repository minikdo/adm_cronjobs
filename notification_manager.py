#!/usr/bin/env python3

import sys
import os.path
from send_email import SendEmail
from string import Template
from db import DB

# import ipdb; ipdb.set_trace()

class NotificationManager:

    def __init__(self):
        self.db = DB()


    def get_ids(self, query):
        return self.db.query(query)


    def generate_body(self, template, ids):

        # load template
        dirname = os.path.dirname(os.path.abspath(__file__))
        body_file = open(os.path.join(dirname, 'templates', '{}.txt'.format(template)), 'r')
        body_content = body_file.read()

        ids2 = ''
        
        for id in ids:
            contract_data = self.db.query("""select n.nazwa, m.nazwa as miasto
            from est e, nazwa n, miasto m 
            where e.miasto=m.id and e.nazwa=n.id
            and e.id = {}""".format(id[0]))

            ids2 += "- {}, {}, {}\n".format(
                id[0],
                contract_data[0][0],
                contract_data[0][1]
            )
            
        # substitute variables
        body_template = Template(body_content)
        body = body_template.substitute(ids=ids2)

        return body


    def notify(self, template, subject, ids):

         # initialize send mail class
         send_email = SendEmail()

         # get user email to notify
         emails = self.db.query("""select nazwa_pelna, email2 from users where aktywna='t'""")
         email_to = [email[0] + ' <' + email[1] + '>' for email in emails]

         body = self.generate_body(template, ids)

         print(body)
         # send mail to active users
         # send_email.send(email_to, subject, body)
         # send_email.quit()

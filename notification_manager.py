#!/usr/bin/env python3

import sys
import os.path
from send_email import SendEmail
from string import Template
from db import DB

# import ipdb; ipdb.set_trace()

class NotificationManager:

    EXPIRED_TEMPLATE = 'expired'
    
    def __init__(self, template):
        self.db = DB()


    def get_template(self, template):
        try:
            # load template
            dirname = os.path.dirname(os.path.abspath(__file__))
            body_file = open(os.path.join(dirname, 'templates', '{}.txt'.format(template)), 'r')
            return body_file.read()
        except OSError as e:
            print('Error: ' + e)
            exit(1)


    def generate_ids(self, ids):
        ids_generated = ''

        for id in ids:
            ids_generated += "- {}, {}, {}\n".format(*id)



    

    def generate_body(self, template, ids, context={}):
        # substitute variables
        body_content = self.get_template(template)
        body_template = Template(body_content)
        context['ids'] = generate_ids(ids)
        body = body_template.substitute(**context)
        
        return body


    def notify(self, subject, body, email_to):

         # initialize send mail class
         send_email = SendEmail()

         print(body)
         # send mail to active users
         # send_email.send(email_to, subject, body)
         # send_email.quit()

#!/usr/bin/env python3

import sys
import os.path
from send_email import SendEmail
from string import Template


class NotificationManager:

    def __init__(self):
        pass


    def get_template(self, template):
        try:
            # load template
            dirname = os.path.dirname(os.path.abspath(__file__))
            body_file = open(os.path.join(dirname, 'templates', '{}.txt'.format(template)), 'r')
            return body_file.read()
        except OSError as e:
            print('Error: ' + e)
            sys.exit(1)


    def generate_ids(self, ids):
        ids_generated = ''

        for id in ids:
            ids_generated += "- "

            for value in id:
                ids_generated += '{}, '.format(value)

            ids_generated += "\n"

        return ids_generated


    def generate_body(self, template, ids, context={}):
        # substitute variables
        body_content = self.get_template(template)
        body_template = Template(body_content)
        context['ids'] = self.generate_ids(ids)
        body = body_template.substitute(**context)
        
        return body


    def notify(self, subject, body, email_to):

         # initialize send mail class
         # send_email = SendEmail()

         print(body)
         # send mail to active users
         # send_email.send(email_to, subject, body)
         # send_email.quit()

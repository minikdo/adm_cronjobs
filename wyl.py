#!/usr/bin/env python3

import sys
import psycopg2
from send_email import send_email
from database import *

try:
    conn = psycopg2.connect(database=DBNAME, user=DBUSER, host=DBHOST)
except:
    print('Błąd dostępu do bazy danych')
    sys.exit(1)

cur = conn.cursor()


def status_change(id):
    "disable contract"
    cur.execute("update est set status=1 where id={}".format(id))


# contracts close to expire 
cur.execute("""select id from est where wyl > now() and 
               wyl < now() + '1 week'::interval and status=0""")
week_left = cur.fetchall()

# expired contracts
cur.execute("select id from est where wyl < now() and status=0")
expired = cur.fetchall()

subject = "kończy się wyłączność oferty"
body = "Kończy się umowa na wyłączność oferty:\n" 

for row in week_left:
    body += "- {} \n".format(row[0])

if expired:
    body += "\nUmowy zakończone:\n"

    for row in expired:
        body += "- {} \n".format(row[0])
        # disable expired contracts
        status_change(row[0])

        # commit changes
        conn.commit()

body += "\nOferty zostaną wkrótce wyłączone\n"

# notify users

# get user email to notify
cur.execute("""select email2 from users where aktywna='t'""")
rows = cur.fetchall()

email_to = []

for email in rows:
    email_to.append(email[0])

# send_email(email_to, subject, body)

print(body)

cur.close()
conn.close()

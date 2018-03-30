import os
import sys
import psycopg2
import json

# import ipdb; ipdb.set_trace()

class DB():

    with open('database.json') as f:
        config = json.loads(f.read())

    def __init__(self):
        self.conn = self.connect(
            self.config['adm']['NAME'],
            self.config['adm']['USER'],
            self.config['adm']['HOST'])
        self.conn2 = self.connect(
            self.config['nie']['NAME'],
            self.config['nie']['USER'],
            self.config['nie']['HOST'])
        self.cur = self.conn.cursor()
        self.cur2 = self.conn2.cursor()

    def connect(self, name, user, host):
        try:
            return psycopg2.connect(
                database=name,
                user=user,
                host=host)
        except:
            print('db {} at {} connect error'.format(name, host))
            sys.exit(1)

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def change_status(self, id, status):
        self.cur.execute("update est set status={} where id={}".format(status, id))
        self.cur2.execute("update oferty_est set status={} where id={}".format(status, id))
        self.conn.commit()
        self.conn2.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
        self.cur2.close()
        self.conn2.close()

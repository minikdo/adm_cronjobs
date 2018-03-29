import os
import sys
import psycopg2

# import ipdb; ipdb.set_trace()


class DB():
    DBNAME = os.environ['DBNAME']
    DBUSER = os.environ['DBUSER']
    DBHOST = os.environ['DBHOST']

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=self.DBNAME,
                user=self.DBUSER,
                host=self.DBHOST)
        except:
            print('db connect error')
            sys.exit(1)
            
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()
            
    def close(self):
        self.cur.close()
        self.conn.close()


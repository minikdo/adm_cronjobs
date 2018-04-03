from db import DB

class BackendService:
    db = DB()

    def change_status(self, id, status):
        self.cur.execute("update est set status={} where id={}".format(status, id))
        self.cur2.execute("update oferty_est set status={} where id={}".format(status, id))
        self.conn.commit()
        self.conn2.commit()

    def expired_ids(self, days_before=0):
        return self.db.query("""select id, cena, pow from est where wyl > now() and
        wyl < now() + '{} days'::interval and status=0""".format(days_before))

    def no_photo_ids(self):
        return self.db.query("""select id, cena, pow from est where zdjecia=0 
        and status=0""")

    def get_active_users(self):
        # get user email to notify
        emails = self.db.query("""select nazwa_pelna, email2 from users where aktywna='t'""")
        return [email[0] + ' <' + email[1] + '>' for email in emails]

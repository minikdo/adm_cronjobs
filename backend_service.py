from db import DB

class BackendService:

    # initialize database connection
    db = DB()

    def change_status(self, id, status):
        self.cur.execute(
            "update est set status={} where id={}".format(status, id)
        )
        self.cur2.execute(
            "update oferty_est set status={} where id={}".format(status, id)
        )
        self.conn.commit()
        self.conn2.commit()

    def expired_ids(self, days_before=0):
        return self.db.query(
            """select id from est where
            wyl < now() + '{} days'::interval
            and status=0""" .format(days_before)
        )

    def photo_count(self):
        ids = self.db.query("""select est.id,count(est_photo.est_id) from est
        left join est_photo on est_photo.est_id = est.id group by est.id
        order by 1""")

        for id in ids:
             self.db.cur.execute(
                 "update est set zdjecia={} where id={}".format(id[1],
                                                                id[0])
             )
             self.db.cur2.execute(
                 "update oferty_est set zdjecia={} where id={}".format(id[1],
                                                                       id[0])
             )

        self.db.conn.commit()
        self.db.conn2.commit()

        return print(ids)

    def no_photo_ids(self):
        return self.db.query("""select id from est where zdjecia=0 
        and status=0""")

    def get_context(self, id):
        return self.db.query("""select n.nazwa, m.nazwa, e.cena, k.nazwisko
        from est e, nazwa n, miasto m, kon k
        where e.nazwa=n.id and e.miasto=m.id and e.id_kon=k.id
        and id={}""".format(id))

    def get_active_users(self):
        # get user email to notify
        emails = self.db.query(
            """select nazwa_pelna, email2 from users where aktywna='t'"""
        )
        return [email[0] + ' <' + email[1] + '>' for email in emails]


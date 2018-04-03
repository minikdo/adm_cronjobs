from db import DB

class BackendService:
    db = DB()

    def get_ids(self, query):
        return self.db.query(query)

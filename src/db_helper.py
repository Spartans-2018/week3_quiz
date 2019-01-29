import sqlite3


class DBhelper():

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)


db = DBhelper("pokedex.db")

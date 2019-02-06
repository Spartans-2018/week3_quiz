import sqlite3


class DBhelper():

    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)

    def execute_query(self, query, *args):
        cursor = self.__conn.cursor()
        return cursor.execute(query, *args)
        # self.conn.close()

    def insert_into(self, query, *args):
        c = self.__conn.cursor()
        c.execute(query, *args)
        self.__conn.commit()
        # self.conn.close()


    # execute write , commit
    # execute batch
db = DBhelper("pokedex.db")

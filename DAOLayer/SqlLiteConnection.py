import sqlite3


class SqlLiteDatabase:

    def get_new_connection(self):
        conn = sqlite3.connect('timeout.db')



import sqlite3
from sqlite3 import Error


class SqlLiteDatabase:

    databaseName = 'timeout.db'

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.databaseName)
            return conn
        except Error as e:
            print(e)

    def create_table(self, conn, create_table_sql_statement):
        try:
            c = conn.cursor()
            c.execute(create_table_sql_statement)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def drop_playlist_table(self, conn ,tableName):
        try:
            c = conn.cursor()
            c.execute('Drop table '+tableName)
        except Error as e:
            print (e)
        finally:
            if conn:
                conn.close()

    def create_playlist_table(self, conn):
        try:
            create_playlist_tbl = 'CREATE TABLE IF NOT EXISTS playlist(' \
                                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                  'songname text not null,'\
                                  'url text not null,'\
                                  'image blob not null'\
                                  ');'
            conn = self.create_connection()
            if conn is not None:
                self.create_table(conn,create_playlist_tbl)
            else:
                print("Error in creation of playlist table")
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


    def insert_data_playlist_table(self,conn, playlistData):
        try:
            sql = 'insert into playlist (songname, url, image) values (?,?,?)'
            cur = conn.cursor()
            cur.execute(sql, playlistData)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def delete_playlist_data_by_name(self, conn, songname):
        try:
            sql = 'delete from playlist where songname = '+songname
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def delete_all_playlist_data(self, conn):
        try:
            sql = 'delete from playlist;'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def fetch_all_playlist_data(self, conn):
        try:
            sql = 'select * from playlist;'
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()

            for row in rows:
                print(row)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


import sqlite3
from TransferObjects.PlaylistData import VideoInfo, UserHistoryInfo
from sqlite3 import Error
import datetime


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

    def create_playlist_table(self):
        try:
            create_playlist_tbl = 'create table if not exists playlist(' \
                                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                  'itemName text not null,' \
                                  'itemUrl text not null);'

            conn = self.create_connection()
            if conn is not None:
                self.create_table(conn,create_playlist_tbl)
            else:
                print("Error in creation of playlist table")
        except Error as e:
            print(e)
        except Exception as ex:
            print(ex)
        finally:
            if conn:
                conn.close()

    def insert_data_playlist_table(self, playlistData):
        try:
            conn = self.create_connection()
            sql = 'insert into playlist (itemName, itemUrl) values (?,?)'
            cur = conn.cursor()
            itemDetails = (playlistData.songname, playlistData.urladdress)
            cur.execute(sql, itemDetails)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def delete_playlist_data_by_name(self,songname):
        print('In delete_playlist_data_by_name:: songname:', songname)
        try:
            conn = self.create_connection()
            sql = 'delete from playlist where itemName = ?'
            cur = conn.cursor()
            input_params = (songname,)
            cur.execute(sql, input_params)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def delete_all_playlist_data(self):
        try:
            conn = self.create_connection()
            sql = 'delete from playlist;'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def fetch_all_playlist_data(self):
        try:
            conn = self.create_connection()
            sql = 'select * from playlist;'
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            videoInfoLst = []
            for row in rows:
                videoInfoLst.append(VideoInfo(row[1], row[2]))

            print(videoInfoLst)
            return videoInfoLst
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def create_history_table(self):
        try:
            create_history_tbl = 'create table if not exists user_history (' \
                                 'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                 '	itemName text not null,' \
                                 'action text not null,' \
                                 'date timestamp);'

            conn = self.create_connection()
            if conn is not None:
                self.create_table(conn,create_history_tbl)
            else:
                print("Error in creation of History table")
        except Error as e:
            print(e)
        except Exception as ex:
            print(ex)
        finally:
            if conn:
                conn.close()

    def insert_data_history_table(self, historyInfo):
        try:
            conn = self.create_connection()
            sql = 'insert into user_history (itemName, action, date) values (?,?,?);'
            cur = conn.cursor()
            historyDetails = (historyInfo.itemName, historyInfo.action, historyInfo.date)
            cur.execute(sql, historyDetails)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def fetch_all_history_data(self):
        try:
            conn = self.create_connection()
            sql = "select itemName, action, strftime('%d-%m-%Y', date) from user_history order by id desc;"
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            historyInfoLst = []
            for row in rows:
                date = datetime.datetime.strptime(row[2], '%d-%m-%Y')
                date = str(datetime.datetime.strftime(date,'%d,%b %Y'))
                historyInfoLst.append(UserHistoryInfo(row[0], row[1], date))

            print(historyInfoLst)
            return historyInfoLst
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def setupBaseDatabaseScripts(self):
        self.create_playlist_table()
        self.create_history_table()

# For testing playlst table
#SqlLiteDatabase().fetch_all_playlist_data()
#videoInfo = VideoInfo('Song Name','http://Some address Testing')
#SqlLiteDatabase().create_playlist_table()
#SqlLiteDatabase().insert_data_playlist_table(videoInfo)
#SqlLiteDatabase().fetch_all_playlist_data()
#SqlLiteDatabase().delete_all_playlist_data()

# For testing History Table
#SqlLiteDatabase().create_history_table()
#userHistoryInfo1 = UserHistoryInfo('songName', 'INSERT', datetime.datetime.now())
#SqlLiteDatabase().insert_data_history_table(userHistoryInfo1)
#SqlLiteDatabase().fetch_all_history_data()
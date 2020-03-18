import os

from ServiceLayer.YoutubeAPI import YoutubeAPI
from ExceptionPackage import TimeOutCustomException as exceptCust
from TransferObjects.PlaylistData import VideoInfo, UserHistoryInfo
from DAOLayer.SqlLiteConnection import SqlLiteDatabase
from datetime import datetime
import webbrowser


class TimeoutService:
    playListData = []
    userHistoryData = []

    def __init__(self):
        # Setting Up basic Database modules
        SqlLiteDatabase().setupBaseDatabaseScripts()
        self.playListData = SqlLiteDatabase().fetch_all_playlist_data()
        self.userHistoryData = SqlLiteDatabase().fetch_all_history_data()
        print('In constructor')

    def get_user_history(self):
        return SqlLiteDatabase().fetch_all_history_data()

    def get_playlist_data(self):
        return SqlLiteDatabase().fetch_all_playlist_data()

    def get_url_info(self):
        return "Code for returning the url and the tumbnail info"

    def get_windows_username(self):
        userName = os.environ['USERNAME']
        print(userName)
        return userName

    def uploadUrl(self, inputUrl):
        if ('www.youtube.com' in inputUrl):
            videoData = YoutubeAPI().getVideoTileAndThumbnail(inputUrl)
            SqlLiteDatabase().insert_data_playlist_table(videoData)
            SqlLiteDatabase().insert_data_history_table(UserHistoryInfo(videoData.songname, 'INSERT', datetime.now()))
            return videoData.songname
        else:
            raise exceptCust.Invalid_Url

    def deletePlaylistItem(self, playlistItem):
        SqlLiteDatabase().delete_playlist_data_by_name(playlistItem)
        SqlLiteDatabase().insert_data_history_table(UserHistoryInfo(playlistItem, 'DELETE', datetime.now()))

    def openURLInBrowser(self,url):
        print('Opening url in the browser:', url)
        webbrowser.open(url)



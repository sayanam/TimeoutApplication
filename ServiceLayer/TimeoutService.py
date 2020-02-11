import os

from ServiceLayer.YoutubeAPI import YoutubeAPI
from ExceptionPackage import TimeOutCustomException as exceptCust


class TimeoutService:

    def get_utl_info(self):
        return "Code for returning the url and the tumbnail info"

    def get_windows_username(self):
        print(os.environ['USERNAME'])

    def getVideoInfo(self, inputUrl):
        videoAPI = YoutubeAPI()
        try:
            videoInfo = videoAPI.getVideoTileAndThumbnail(inputUrl)
        except exceptCust.Invalid_Url:
            return "Invalid URL !!"
        except exceptCust.GeneralException:
            return "Error Occurred. Contact the Application administrator"

    #def storeVideoInfo(self):

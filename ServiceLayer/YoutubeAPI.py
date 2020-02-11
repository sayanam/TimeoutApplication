import googleapiclient.discovery
from TransferObjects import PlaylistData
import ExceptionPackage.TimeOutCustomException  as excepCust
from PIL import Image
import requests
from io import BytesIO
import url_parser

class YoutubeAPI:

    def getYoutubeObject(self):
        DEVELOPER_KEY = "AIzaSyAzOKbNS2YjXH05mn_HxrGYuPSTow37jGI"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        return googleapiclient.discovery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                        developerKey=DEVELOPER_KEY)

    def getImageFromURL(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(BytesIO('sampleFileName.jpg')) # untested code, verify!!!
        return img

    def getVideoId(self, url):
        url_data = url_parser.parse_url(url)
        try:
            return url_data['query']['v']
        except KeyError:
            raise excepCust.Invalid_Url()

    def getRespFromAPIVideosList(self,videoId):
        print("In getRespFromAPIVideosList method. Input videoId = {}".format(videoId))
        request = self.getYoutubeObject().videos().list(part="snippet,contentDetails,statistics", id=videoId)
        response = request.execute()
        print("response ::", response)

        return response

    def getVideoTileAndThumbnail(self, urlInput):
        video_id = self.getVideoId(urlInput)
        response = self.getRespFromAPIVideosList(video_id)
        try:
            totalResultCount = int(response['pageInfo']['resultsPerPage'])
            if totalResultCount == 0:
                raise excepCust.Invalid_Url()
            else:
                title = response['items'][0]['snippet']['title']
                img = self.getImageFromURL(response['items'][0]['snippet']['thumbnails']['default']['url'])
                videoInfo = PlaylistData.VideoInfo(title, img, urlInput)
                return videoInfo
        except excepCust.Invalid_Url:
            raise excepCust.Invalid_Url()
        except Exception:
            raise excepCust.GeneralException()

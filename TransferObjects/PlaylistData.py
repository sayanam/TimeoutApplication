class VideoInfo:

    def __init__(self, songname, urladdress):
        self.songname = songname
        self.urladdress = urladdress

class UserHistoryInfo:

    def __init__(self, itemName, action,date):
        self.date = date
        self.action = action
        self.itemName = itemName

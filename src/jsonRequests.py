import requests
from settings import CHANNEL_ID

def getJSON():
    url = "https://api.twitch.tv/helix/streams?user_id=" + CHANNEL_ID
    response = ""
    while True:
        try:            
            return requests.get(url).json()
        except Exception, err:
            print Exception, err

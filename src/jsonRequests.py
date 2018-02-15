def getJSON(channel):
    url = "https://api.twitch.tv/kraken/streams?channel=" + channel
    while True:
        try:            
            return requests.get(url).json()
        except Exception, err:
            print Exception, err
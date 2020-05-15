import requests

def go():
    url = 'https://feed2json.org/convert?url=https%3A%2F%2Fwww.youtube.com%2Ffeeds%2Fvideos.xml%3Fchannel_id%3DUCz64Q7H4zuxVCCGKNoCAX1A'

    data = requests.get(url).json()

    videos = data['items']
    datas = []
    for vid in videos:
        vds = dict(
            img='https://i.ytimg.com/vi/'+vid['guid'].split(':')[-1]+'/hqdefault.jpg',
            title=vid['title'],
            url=vid['url'],
            date=vid['date_published'])
        datas.append(vds)

    return datas

def subdat():
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCz64Q7H4zuxVCCGKNoCAX1A&key=AIzaSyBqYHodO3rwDFeu6DFskyge3Hoa0LFIOSg'

    d = requests.get(url).json()

    stat = (d['items'][0]['statistics'])
    d = dict(
        views=stat['viewCount'],
        sub=stat['subscriberCount'],
        videos=stat['videoCount'])
    return d


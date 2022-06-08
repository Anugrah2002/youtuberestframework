import urllib.request
from bs4 import BeautifulSoup

def articleContent():
    print('line 47')
    try:

        req = urllib.request.Request(
            'https://www.aajtak.in/entertainment/television/story/taarak-mehta-ka-oolath-chashmah-sunderlal-jethalal-dayaben-return-video-impress-fans-tmov-1477918-2022-06-07',
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        articlePara = getImage(soup)
        # print('line 55')
        print(articlePara)
        print('line 57')
        return 'ok'
    except Exception as e:
        print(e)

def getImage(soup):
    try:
        articletitle = soup.find("div",{"class":"main-img"})
        print('line 30')
        # print(articletitle)
        img = articletitle.find("img",{"class":"lazyload"})
        image = img['data-src']
        print(image)
        imagedown = urllib.request.urlretrieve(image,'image.jpg')
        # print(articletitle)
        # for i in articletitle:
        #     articletitle = i.get_text()
        #     # print(articletitle)
        return 'ok'
    except Exception as e:
        print(e)



articleContent()
import urllib.request
from bs4 import BeautifulSoup

def articleContent():
    try:

        req = urllib.request.Request(
            'https://www.aajtak.in/entertainment/television/photo/uorfi-javed-slams-report-of-showing-nipples-how-to-avoid-oops-moment-revealing-dress-tmov-1478365-2022-06-08-2',
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        articlePara = getImageUrl(soup)
        # print('line 55')
        # print(articlePara)
        print('line 57')
        return 'ok'
    except Exception as e:
        print(e)




def getImageUrl(soup):
    try:

        print('line 32')
        imageformurl = soup.find("div",{"class":"main-img"})
        img = imageformurl.find("img",{"class":"lazyload"})
        image_url = img['data-src']
        print(image_url)
        # imagedown = urllib.request.urlretrieve(image,'image.jpg') # this is for downloading the image from the url and save it to the current folder by the name which is in string(for ex: image.jpg)
        return image_url
    except Exception as e:
        print(e)








articleContent()
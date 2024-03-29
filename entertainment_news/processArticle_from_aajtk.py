# import urllib.request
import xmltodict
# from bs4 import BeautifulSoup
from . import models
import re
import urllib.request
from bs4 import BeautifulSoup


def dataFromThearticles():
    try:
        title = ""
        content = ""
        summary = ""
        YTtitle = ""
        unique_url = ""
        image_url = ""
        url_list = []
        url = 'https://www.aajtak.in/entertainment/television'
        req = urllib.request.Request(
            url,
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        content = soup.find("div", {"class": "at_row"})
        content = content.find("div", {"class": "content-area"})
        content = content.find("div", {"class": "section-listing-LHS"})
        url_of_the_articles = content.find_all("div", {"class": "widget-listing"})

        for i in url_of_the_articles:
            url = i.find_all('a')
            urls = url[0]['href']
            url_list.append(urls)
            # print(url_list)
        unique_url = getUniqueArticle(url_list)
        print('line 41')
        return articleContent(title, content, summary, YTtitle, image_url, unique_url)
    except Exception as e:
        print(e)


def articleContent(title, content, description, YTtitle, image_url, url):
    print('line 47')
    try:
        print(url)
        req = urllib.request.Request(
            url,
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        articlePara = getArticlePara(soup)
        print('line 55')
        print(articlePara)
        # print('line 57')
        articletitle = getArticleTitle(url)
        print(articletitle)
        print('line 60')
        description = getArticleTitle(url)
        print(description)
        print('line 63')
        image_url = getImageUrl(soup)
        # print(image_url)
        # print('line 75')
        Yttitle = YtTitle(soup)

        print(Yttitle)
        print('line 67')
        # print(Yttitle)

        return articletitle,articlePara, description, Yttitle, image_url
    except Exception as e:
        print(e)


def getArticlePara(soup):
    try:
        content = soup.find_all("p")
        sorted_content = removeUnwantedWords(content)
        return sorted_content
    except Exception as e:
        print(e)



def getArticleTitle(url):
    try:
        s = url.split('/')[-1]
        s = s.replace('-', ' ')
        s = s.split('tmov')
        title_from_url = str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s[0]))
        return title_from_url
    except Exception as e:
        print(e)



def YtTitle(soup):
    try:
        articletitle = soup.find_all("h1")
        for i in articletitle:
            articletitle = i.get_text()
            # print(articletitle)
            return articletitle
    except Exception as e:
        print(e)




def getUniqueArticle(unique_url):
    print('line 121')
    for url in unique_url:
        try:
            s = url.split('/')[-1]
            s = s.replace('-', ' ')
            s = s.split('tmov')
            title_from_url = str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s[0]))
            obj = models.entertainmentNewsdb_for_aajtk.objects.get(title=title_from_url)
            print('line 124')
            print(obj)
            print('line 126')
        except models.entertainmentNewsdb_for_aajtk.DoesNotExist:
            return url


def getImageUrl(soup):
    try:
        imageformurl = soup.find("div",{"class":"main-img"})
        img = imageformurl.find("img",{"class":"lazyload"})
        image_url = img['data-src']
        print(image_url)
        # imagedown = urllib.request.urlretrieve(image,'image.jpg') # this is for downloading the image from the url and save it to the current folder by the name which is in string(for ex: image.jpg)
        return image_url
    except Exception as e:
        print(e)




def removeUnwantedWords(content):
    para = ""
    for words in content:
        unwanted_words = words.find('a')
        if (unwanted_words != None):
            unwanted_words.decompose()
        else:
            para = para + words.get_text()
    return para








#-----------------------------------------
# ----------------------------------------









# dataFromThearticles()
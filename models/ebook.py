from datetime import datetime
from bs4 import BeautifulSoup
import requests


class EbookModel():
    def __init__(self, url):
        self.url = url
        print('url is {}'.format(url))
        print('self.url is {}'.format(self.url))
        self.title = ''
        self.description = ''
        self.image = ''
        self.date = ''


    def json(self):
        return({"date": self.date,
                "title": self.title,
                "description": self.description,
                "image_src": self.image
        })

    def get(self):
        print(self.url)
        agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        resp = requests.get(self.url, headers=agent)
        #print ("Requests repponse:{}".format(resp.status_code))

        soup = BeautifulSoup(resp.text, 'html.parser')
        dotd = soup.select('.dotd-title')
        self.title = dotd[0].text.strip()
        self.description = soup.find("div", class_="dotd-main-book-summary float-left").select("div")[2].text.strip()
        dotd_image = soup.find("div", class_="dotd-main-book-image float-left")
        self.image_src = "https:"+dotd_image.a.noscript.img.get('src')
        dt = datetime.now()
        self.date = dt.strftime("%Y-%m-%d %H:%M")

        return self

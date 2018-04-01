from flask_restful import Resource
from datetime import datetime
from bs4 import BeautifulSoup
import requests

class Ebook(Resource):

    def get(self):
        url = "https://www.packtpub.com/packt/offers/free-learning"
        agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        resp = requests.get(url, headers=agent)
        #print ("Requests repponse:{}".format(resp.status_code))

        soup = BeautifulSoup(resp.text, 'html.parser')
        dotd = soup.select('.dotd-title')
        title = dotd[0].text.strip()
        description = soup.find("div", class_="dotd-main-book-summary float-left").select("div")[2].text.strip()
        dotd_image = soup.find("div", class_="dotd-main-book-image float-left")
        image_src = "https:"+dotd_image.a.noscript.img.get('src')
        dt = datetime.now()
        date = dt.strftime("%Y-%m-%d %H:%M")

        ebook = {"date": date,
                "title": title,
                "description": description,
                "image_src": image_src
        }


        return ebook

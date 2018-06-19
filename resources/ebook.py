from flask_restful import Resource
from models.ebook import EbookModel


class Ebook(Resource):

    def get(self):
        # url = 'https://www.packtpub.com/packt/offers/free-learning'

        return EbookModelDB().get()

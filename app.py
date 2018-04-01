from flask import Flask
from flask_restful import Api
from resources.ebook import Ebook


app = Flask(__name__)
api = Api(app)

api.add_resource(Ebook, '/ebook')

if __name__=='__main__':
    app.run(port=5001, debug=True)

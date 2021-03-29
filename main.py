from flask import Flask
from flask_restful import Api, Resource
from quotes_scrapper import spacequotes, spacequotes1
import random

app = Flask(__name__)
api = Api(app)

class quotes1(Resource):
    def get(self):
        quotes = spacequotes1()
        return {"quotes" : quotes}

class quotes2(Resource):
    def get(self):
        quotes = spacequotes()
        return {"quotes" : quotes}

class randomQuote(Resource):
    def get(self):
        list = [1, 2]
        choice = random.choice(list)

        if choice == 1:
            quotes = spacequotes()
            boom = random.choice(quotes)
        else: 
            quotes = spacequotes1()
            boom = random.choice(quotes)

        return {"quote": boom}

api.add_resource(quotes1, "/quotes1")
api.add_resource(quotes2, "/quotes2")
api.add_resource(randomQuote, "/random")

if __name__ == "__main__":
    app.run(debug=True)

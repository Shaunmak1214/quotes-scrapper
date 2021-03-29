from flask import Flask
from flask_restful import Api, Resource
from quotes_scrapper import spacequotes

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        quotes = spacequotes()
        return {"data" : quotes}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)

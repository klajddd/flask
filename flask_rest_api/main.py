from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return {"data": "Hello World"}

#     def get(self, name, age):
#         return {"name": name, "age": age}

#     def post(self):
#         return {"data": "Posted"}


# api.add_resource(HelloWorld, "/helloworld")
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")


videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

api.add_resource(Video, "/video")


if __name__ == "__main__":
    app.run(debug=True)

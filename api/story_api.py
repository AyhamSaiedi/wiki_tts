from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

titles = {'kirche 1': {'coords': '188, 992', 'summary': 'text bla bla...', 'language': 'de'},
        'kirche 2': {'coords': '988, 342', 'summary': 'text again again...', 'language': 'de'}}

class Story(Resource):
    def get(self, title):
        return titles[title]

api.add_resource(Story, '/summary/<string:title>')

if __name__ == "__main__":
    app.run(debug=True)



# channels = {}
# storys = {}

# def abort_if_channel_does_not_exist(channel_id):
#     if channel_id not in channels:
#         abort(404, message="Channel does not exist")

# def abort_if_story_does_not_exist(story_id):
#     if story_id not in storys:
#         abort(404, message="story does not exist")

# def abort_if_channel_does_exist(channel_id):
#     if channel_id not in channels:
#         abort(409, message="A channel with this ID already exists")

# def abort_if_story_does_exist(story_id):
#     if story_id not in storys:
#         abort(409, message="A story with the same ID already exists")


# # arg parser
# story_create_args = reqparse.RequestParser()
# story_create_args.add_argument("titel", type=str, help="Titel of the story")
# story_create_args.add_argument("summary", type=str, help="Summary of the story")
# story_create_args.add_argument("coordinates", type=str, help="Coordinates of the story")

# class Channel(Resource):
#     def get(self, channel_id):
#         abort_if_channel_does_not_exist(channel_id)
#         return channels[channel_id]
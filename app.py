# app.py

from models import db
from flask import Flask
from flask_migrate import Migrate
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from post import Post
from comment import Comment
from user import UserApi
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

migrate = Migrate(app, db)

api = Api(app)

api.add_resource(Post, '/posts', '/posts/<int:post_idx>')
api.add_resource(Comment, '/comments', '/comments/<int:comment_idx>')
api.add_resource(UserApi, '/users')

if __name__ == '__main__':
  app.run(debug=True)
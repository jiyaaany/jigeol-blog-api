# app.py

from models import db
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from post import Post, Posts
from user import UserApi
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

api = Api(app)

api.add_resource(Post, '/posts/<int:post_idx>')
api.add_resource(Posts, '/posts')

api.add_resource(UserApi, '/users')

if __name__ == '__main__':
  app.run(debug=True)

# api = Api(app)

# @app.route('/')
# def hello():
#   return "Hello World!"

# @api.route('/post')
# class Post(Resource):
#   def post(self):
#     return {"post": "posts"}

# @api.route('/post/<int:id>')
# class Post(Resource):
#   def get(self, id):
#     return {"post": "hello"}

#   def put(self, id):
#     return {"method": "put"}

#   def delete(self, id):
#     return {"method": "delete"}

# # @app.teardown_appcontext
# # def shutdown_session(exception=None):
  
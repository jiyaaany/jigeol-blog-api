from flask.globals import request
from flask_restful import Resource
from models import PostModel, db

class Post(Resource):
  def get(self, post_idx):
    return {"method": "get"}

  def put(self, post_idx):
    data = request.get_json()
    print(data['title'])
    print(data['content'])
    
    return {"method": "put"}

  def delete(Self, post_idx):
    return {"method": "delete"}

class Posts(Resource):
  def post(self):
    try:
      post_data = request.get_json()
      post = PostModel(
        post_data['title'],
        post_data['content'],
        post_data['user_idx']
      )
      db.session.add(post)
      db.session.commit()
    except Exception as e:
      print(str(e))

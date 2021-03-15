from flask.globals import request
from flask_restful import Resource
from models import PostModel, db
import pandas, json, datetime

class Post(Resource):
  def get(self, post_idx):
    query = db.session.query(PostModel).filter(PostModel.post_idx == post_idx)
    pandas_query = pandas.read_sql(query.statement, query.session.bind)

    post = json.loads(pandas_query.to_json(orient='records'))
    print(post[0]['reg_date'])
    print(post[0]['reg_date'].strftime('%Y-%m-%d %H:%M:%S'))
    return post

  def put(self, post_idx):
    data = request.get_json()
    print(data['title'])
    print(data['content'])
    
    return {"method": "put"}

  def delete(self, post_idx):
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

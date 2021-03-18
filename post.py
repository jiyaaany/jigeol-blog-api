from flask.globals import request
from flask_restful import Resource
from models import PostModel, db
import pandas, json
from datetime import datetime

class Post(Resource):
  def get(self, post_idx):
    post = db.session.query(PostModel).filter(PostModel.post_idx == post_idx).first()
    
    return {
      'id': post.post_idx,
      'title': post.title,
      'content': post.content,
      'reg_date': str(post.reg_date),
      'user_idx': post.user_idx
    }

  def put(self, post_idx):
    if request.get_json():
      post_data = request.get_json()
      post = db.session.query(PostModel).filter(PostModel.post_idx == post_idx).first()

      for key in list(post_data.keys()):
        post[key] = post_data[key]

      db.session.commit()

    return {
      'status': 200,
      'message': '수정되었습니다.'
    }

  def delete(self, post_idx):
    post = db.session.query(PostModel).filter(PostModel.post_idx == post_idx).first()
    db.session.delete(post)
    db.session.commit()
      
    return {
      'status': 200,
      'message': '삭제되었습니다.'
    }

class Posts(Resource):
  def post(self):
    try:
      if request.get_json():
        post_data = request.get_json()
        post = PostModel(
          post_data['title'],
          post_data['content'],
          post_data['user_idx']
        )
        db.session.add(post)
        db.session.commit()

        #psycopg2.errors.ForeignKeyViolation
        return {
          'status': 200,
          'message': '저장되었습니다.'
        }
      else:
        query = db.session.query(PostModel)
        pandas_query = pandas.read_sql(query.statement, query.session.bind)
        posts = json.loads(pandas_query.to_json(orient='records'))

        for post in posts:
          post['reg_date'] = str(datetime.fromtimestamp(post['reg_date']/1000))

        return posts
    except Exception as e:
      print(str(e))

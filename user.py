from flask.globals import request
from flask_restful import Resource
from models import User, db
import bcrypt

class UserApi(Resource):
  def post(self):
    user_data = request.get_json()
    user = User(
      user_data['user_id'],
      user_data['email'],
      bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()),
      user_data['name'].encode('utf-8'),
      user_data['nick_name'].encode('utf-8')
    )
    db.session.add(user)
    db.session.commit()
    
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'

  user_idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.String(128), unique=True, nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(512), nullable=False)
  name = db.Column(db.String(128), nullable=False)
  nick_name = db.Column(db.String(128))
  token = db.Column(db.String(512))
  reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, user_id, email, password, name, nick_name):
      self.user_id = user_id
      self.email = email
      self.password = password
      self.name = name
      self.nick_name = nick_name


class PostModel(db.Model):
  __tablename__ = 'post'

  post_idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text)
  reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  user_idx = db.Column(db.Integer, db.ForeignKey('user.user_idx'), nullable=False)

  def __init__(self, title, content, user_idx):
    self.title = title
    self.content = content
    self.user_idx = user_idx

class Comment(db.Model):
  __tablename__ = 'comment'

  comment_idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
  content = db.Column(db.Text)
  reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  user_idx = db.Column(db.Integer, db.ForeignKey('user.user_idx'), nullable=False)
  post_idx = db.Column(db.Integer, db.ForeignKey('post.post_idx'), nullable=False)
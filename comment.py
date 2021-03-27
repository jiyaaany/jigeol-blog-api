from flask_restful import Resource
from flask.globals import request
from models import CommentModel, db
import pandas, json

class Comment(Resource):
    def post(self):
        if request.get_json():
            comment_data = request.get_json()
            comment = CommentModel(
                comment_data['content'],
                comment_data['user_idx'],
                comment_data['post_idx']
            )

            db.session.add(comment)
            db.session.commit()

            return {
                'status': 200,
                'message': '댓글이 입력되었습니다.'
            }
        else:
            query = db.session.query(CommentModel)
            pandas_query = pandas.read_sql(query.statement, query.session.bind)
            comments = json.loads(pandas_query.to_json(orient='records'))

            return comments

    def get(self, post_idx):
        query = db.session.query(CommentModel).filter(CommentModel.post_idx==post_idx)
        pandas_query = pandas.read_sql(query.statement, query.session.bind)
        comments = json.loads(pandas_query.to_json(orient='records'))
        
        return comments if comments else []
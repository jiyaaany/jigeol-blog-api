from flask_restful import Resource
from flask.globals import request
from models import CommentModel, db
from datetime import datetime
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
            db.session.refresh(comment)
            print(comment.comment_idx)

            return {
                'status': 200,
                'message': '댓글이 입력되었습니다.',
            }

        else:
            query = db.session.query(CommentModel)
            pandas_query = pandas.read_sql(query.statement, query.session.bind)
            comments = json.loads(pandas_query.to_json(orient='records'))

            return comments

    def get(self, comment_idx):
        comment = db.session.query(CommentModel).filter(CommentModel.comment_idx == comment_idx).first()

        print(type(comment))
        print(json.dumps(comment))
        print(json.dump(comment))

        if comment:
            return 200
        else:
            return {
                'status': 404,
                'message': '댓글이 없습니다.',
            }

    def delete(self, comment_idx):
        comment = db.session.query(CommentModel).filter(CommentModel.comment_idx == comment_idx).first()
        db.session.delete(comment)
        db.session.commit()

        return {
            'status': 200,
            'message': '댓글이 삭제되었습니다.'
        }
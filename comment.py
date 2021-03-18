from flask_restful import Resource
from flask.globals import request
from models import CommentModel, db

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

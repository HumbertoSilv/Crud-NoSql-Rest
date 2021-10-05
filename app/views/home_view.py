from app.exceptions.post_exceptions import IncorrectDataError, NotFoundId
from app.models.post_models import Post
from flask import Flask, jsonify, request


def init_app(app: Flask):
    @app.post("/posts")
    def create_post():
        data = request.json
        try:
            new_post = Post(**data)
            saved = new_post.save_post()
        except (IncorrectDataError, TypeError):
            return {"msg": "Incorrect data"}, 400

        return jsonify(saved), 201

    @app.delete("/posts/<int:id>")
    def delete_post(id: int):
        try:
            post_deleted = Post.post_delete(id)
        except NotFoundId:
            return {"msg": f"Not Found Posts By ID: {id}"}, 404

        return jsonify(post_deleted), 200

    @app.get("/posts/<int:id>")
    def read_post_by_id(id: int):
        try:
            post = Post.post_by_id(id)
        except NotFoundId:
            return {"msg": f"Not Found Posts By ID: {id}"}, 404

        return jsonify(post), 200

    @app.get("/posts")
    def read_posts():
        post_list = Post.all_posts()
        return jsonify(post_list), 200

    @app.patch("/posts/<int:id>")
    def update_post(id: int):
        data = request.json
        try:
            post_update = Post.post_update(id, data)
        except NotFoundId:
            return {"msg": f"Not Found Posts By ID: {id}"}, 404

        except IncorrectDataError:
            return {"msg": "Incorrect Keys"}, 400

        return jsonify(post_update), 200

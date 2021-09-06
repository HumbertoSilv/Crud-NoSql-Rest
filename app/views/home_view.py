from flask import Flask


def init_app(app: Flask):
    @app.post("/posts")
    def create_post():
        ...

    @app.delete("/posts/<int:id>")
    def delete_post(id: int):
        ...
    
    @app.get("/posts/<int:id>")
    def read_post_by_id(id: int):
        ...

    @app.get("/posts")
    def read_posts(id: int):
        ...

    @app.patch("/posts/<int:id>")
    def update_post(id: int):
        ...
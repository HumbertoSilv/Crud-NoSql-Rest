from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.views import home_view
    home_view.init_app(app)

    return app

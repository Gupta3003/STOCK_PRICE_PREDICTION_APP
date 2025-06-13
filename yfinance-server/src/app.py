from flask import Flask
from .db import initDb

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config')
    initDb(app)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from . import auth
    app.register_blueprint(auth.bp)

    from . import stock
    app.register_blueprint(stock.bp)

    return app
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy

from config import config
from .new_word_notebook import load_new_words

bootstrap = Bootstrap()
# db = SQLAlchemy()
cors = CORS()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    # db.init_app(app)
    cors.init_app(app)

    load_new_words('./extern/new_words.json')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .mathematics import main as mathematics_blueprint
    app.register_blueprint(mathematics_blueprint)

    from .english import main as english_blueprint
    app.register_blueprint(english_blueprint)

    return app

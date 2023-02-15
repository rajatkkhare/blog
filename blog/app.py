from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from blog.api.deps import api_errors

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()
ma = Marshmallow()
api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_bp, catch_all_404s=True, errors=api_errors())


def create_app():
    app.config.from_pyfile("settings.py")

    @app.before_first_request
    def create_tables():
        db.create_all()

    register_libraries()
    register_blueprints()
    register_api_resources()
    return app


def register_libraries():
    db.init_app(app)
    ma.init_app(app)
    register_models_for_migration()


def register_blueprints():
    app.register_blueprint(api_bp)


def register_models_for_migration():
    from blog.models import Article


def register_api_resources():
    from blog.api.v1.Articles import Articles

    api.add_resource(Articles, "/articles")

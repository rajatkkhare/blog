import os


DEBUG = os.environ.get("FLASK_DEBUG", True)
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL", "mysql+pymysql://root:root@localhost:3306/blog"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

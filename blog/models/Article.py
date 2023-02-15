from datetime import datetime

from sqlalchemy import JSON

from blog.ResourceMixin import ResourceMixin
from blog.app import db


class Article(ResourceMixin, db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text())
    is_published = db.Column(db.Boolean, nullable=False, default=False)
    tags = db.Column(JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    published_at = db.Column(db.DateTime)

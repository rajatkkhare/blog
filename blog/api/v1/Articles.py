from datetime import datetime

from flask import request
from flask_restful import Resource

from blog.api.deps import api_resp
from blog.models.Article import Article
from blog.schema.ArticleSchema import ArticleSchema


class Articles(Resource):
    def get(self):
        article_id = request.args.get("article_id")
        if article_id:
            data = Article.query.filter_by(id=article_id).first()
            if not data:
                return api_resp(404, "Article not found.")
            article_schema = ArticleSchema()
        else:
            data = Article.query.all()
            article_schema = ArticleSchema(many=True)
        return api_resp(200, article_schema.dump(data))

    def post(self):
        data = request.get_json()
        errors = ArticleSchema().validate(data)
        if errors:
            return api_resp(400, errors)
        article = ArticleSchema().load(data)
        if article.is_published:
            article.published_at = datetime.now()
        return api_resp(201, ArticleSchema().dump(article.save()))

    def put(self):
        article_id = request.args.get("article_id")
        if not article_id:
            return api_resp(400, {"article_id": "Is required in query string parameters."})

        data = request.get_json()
        errors = ArticleSchema().validate(data)
        if errors:
            return api_resp(400, errors)

        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return api_resp(404, "Article not found.")

        article_schema = ArticleSchema().load(data)
        if article_schema.is_published and not article.is_published:
            article.published_at = datetime.now()
        if article_schema.is_published is not None:
            article.is_published = article_schema.is_published
        article.title = article_schema.title
        article.body = article_schema.body
        article.tags = article_schema.tags
        return api_resp(200, ArticleSchema().dump(article.save()))

    def delete(self):
        article_id = request.args.get("article_id")
        if not article_id:
            return api_resp(400, {"article_id": "Is required in query string parameters."})
        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return api_resp(404, "Article not found.")
        article.delete()
        return api_resp(200, "Article deleted successfully.")

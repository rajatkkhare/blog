from blog.app import ma
from blog.models.Article import Article


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        load_instance = True

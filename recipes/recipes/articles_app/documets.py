# register "Documents" for elastic search

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from articles_app.models import ArticleType, Article
from users_app.models import User


@registry.register_document
class UserDocument(Document):
    class Index:
        name = "users"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        ]


@registry.register_document
class ArticleTypeDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = "article_type"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = ArticleType
        fields = [
            "title",
        ]


@registry.register_document
class ArticleDocument(Document):
    type = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "title": fields.TextField(),
    })
    title = fields.TextField(attr="type_to_string")

    class Index:
        name = "articles"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Article
        fields = [
            "title",
            "description",
            "created",
            "updated",
        ]

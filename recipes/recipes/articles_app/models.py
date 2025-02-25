from django.db import models

from core.models import BaseModel


class ArticleType(models.Model):
    title = models.CharField()

    class Meta:
        verbose_name = "Article's Type"
        verbose_name_plural = "Article's Types"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField()
    topic = models.CharField(blank=True, null=True)
    type = models.ForeignKey(to="articles_app.ArticleType", on_delete=models.CASCADE)
    description = models.TextField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

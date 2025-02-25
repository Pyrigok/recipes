from django.contrib import admin

from articles_app.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Article, ArticleAdmin)

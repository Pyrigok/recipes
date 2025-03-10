# Generated by Django 5.1.3 on 2025-01-27 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles_app", "0002_article_topic_article_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField()),
            ],
            options={
                "verbose_name": "Article's Type",
                "verbose_name_plural": "Article's Types",
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="articles_app.articletype",
            ),
        ),
    ]

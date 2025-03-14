# Generated by Django 5.1.3 on 2025-01-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes_app", "0003_recipe_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="fruit",
            name="weight",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="meat",
            name="weight",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="sauce",
            name="weight",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="vegetable",
            name="weight",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

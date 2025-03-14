# Generated by Django 5.1.3 on 2025-01-08 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseModel",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Fruit",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
            options={
                "verbose_name": "Fruit",
                "verbose_name_plural": "Fruits",
            },
            bases=("recipes_app.basemodel",),
        ),
        migrations.CreateModel(
            name="Meat",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("філе", "Fillet"),
                            ("шия", "Neck"),
                            ("шинка", "Ham"),
                            ("вирізка", "Tenderloin"),
                            ("нога", "Leg"),
                            ("бедро", "Thigh"),
                            ("ребро", "Ribs"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
            options={
                "verbose_name": "Meat",
                "verbose_name_plural": "Meat",
            },
            bases=("recipes_app.basemodel",),
        ),
        migrations.CreateModel(
            name="Sauce",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("receipt", models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                "verbose_name": "Souce",
                "verbose_name_plural": "Souce",
            },
            bases=("recipes_app.basemodel",),
        ),
        migrations.CreateModel(
            name="Vegetable",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
            options={
                "verbose_name": "Vegetable",
                "verbose_name_plural": "Vegetables",
            },
            bases=("recipes_app.basemodel",),
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Salad", "Salad"),
                            ("Soup", "Soup"),
                            ("Main course", "Main Course"),
                            ("Dessert", "Dessert"),
                        ]
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "cooking_type",
                    models.CharField(choices=[("Mix", "Mix"), ("Boil", "Boil")]),
                ),
                ("receipt", models.TextField(blank=True, max_length=5000, null=True)),
                ("is_allowed_for_pregnant", models.BooleanField(default=False)),
                (
                    "fruits",
                    models.ManyToManyField(
                        related_name="recipe", to="recipes_app.fruit"
                    ),
                ),
                (
                    "meat",
                    models.ManyToManyField(
                        related_name="recipe", to="recipes_app.meat"
                    ),
                ),
                (
                    "sauce",
                    models.ManyToManyField(
                        related_name="recipe", to="recipes_app.sauce"
                    ),
                ),
                (
                    "vegetables",
                    models.ManyToManyField(
                        related_name="recipe", to="recipes_app.vegetable"
                    ),
                ),
            ],
            options={
                "verbose_name": "Dish",
                "verbose_name_plural": "Dishes",
            },
            bases=("recipes_app.basemodel",),
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="recipes_app.basemodel",
                    ),
                ),
                ("picture", models.ImageField(upload_to="")),
                (
                    "receipt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_app.recipe",
                    ),
                ),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
            },
            bases=("recipes_app.basemodel",),
        ),
    ]

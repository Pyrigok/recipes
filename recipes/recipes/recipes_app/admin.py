from django.contrib import admin

from recipes_app.models import Vegetable, Fruit, Sauce, Meat, Recipe


class VegetableAdmin(admin.ModelAdmin):
    list_display = ["title", "weight"]
    ordering = ["title", "weight"]


class FruitAdmin(admin.ModelAdmin):
    list_display = ["title", "weight"]
    ordering = ["title", "weight"]


class MeatAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "weight"]
    ordering = ["title", "weight"]


class SauceAdmin(admin.ModelAdmin):
    list_display = ["title", "weight"]
    ordering = ["title", "weight"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "is_allowed_for_pregnant"]
    ordering = ["title", "type", "is_allowed_for_pregnant"]


admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Sauce, SauceAdmin)
admin.site.register(Meat, MeatAdmin)
admin.site.register(Recipe, RecipeAdmin)

from django.contrib import admin

from rest_app.models import Movie, Genre, TravelPlan


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "is_for_kids_allowed", "is_for_adult_only"]
    ordering = ["title", "type", "is_for_kids_allowed", "is_for_adult_only"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]


class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ["title", "date_start", "date_finish", "is_completed"]
    ordering = ["title", "date_start", "date_finish", "is_completed"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(TravelPlan, TravelPlanAdmin)

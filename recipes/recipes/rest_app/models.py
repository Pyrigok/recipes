from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model):
    class TypeChoices(models.TextChoices):
        film = "Film"
        serial = "Serial"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True, blank=True)
    type = models.CharField(choices=TypeChoices, default=TypeChoices.film)
    genre = models.ManyToManyField(to=Genre, related_name="genre_of_movie")
    url = models.URLField(null=True, blank=True)
    is_for_kids_allowed = models.BooleanField(default=False)
    is_for_adult_only = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title}"


class TravelPlan(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    impression = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "TravelPlan"
        verbose_name_plural = "TravelPlans"

    def __str__(self):
        return f"{self.title}"

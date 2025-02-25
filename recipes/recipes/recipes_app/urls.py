from rest_framework import routers
from django.urls import path, include
from recipes_app.views import RecipeViewSet, InfoView, MeatInfoView


app_name = "recipes_app"

router = routers.SimpleRouter()

router.register("", RecipeViewSet, basename="recipes")

urlpatterns = [

    path("info/", InfoView.as_view(), name="info"),
    path("meat/info/", MeatInfoView.as_view(), name="meat-info"),
    path("", include(router.urls)),
]

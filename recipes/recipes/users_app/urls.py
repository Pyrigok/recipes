from rest_framework import routers
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from users_app import views


router = routers.SimpleRouter()

router.register("", views.UsersViewSet, basename="users")

urlpatterns = [
    path(
        "auth/login/",
        LoginView.as_view(template_name="users/login.html"),
        name="user-login"
         ),
    path("auth/logout/", LogoutView.as_view(), name="user-logout"),
    path("", include(router.urls)),
]

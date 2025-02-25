import os

from decouple import config
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipes.settings")
app = Celery("recipes")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

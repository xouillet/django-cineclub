from django.apps import AppConfig
from django.conf import settings


class CineConfig(AppConfig):
    name = "cine"
    verbose_name = settings.CINECLUB_NAME

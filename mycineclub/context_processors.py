from django.conf import settings


def name(request):
    return {"cineclub_name": settings.CINECLUB_NAME}

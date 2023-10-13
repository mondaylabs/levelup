from datetime import timedelta

from django.conf import settings
from django.utils import timezone


def expires_default():
    return timezone.now() + timedelta(seconds=settings.TOKEN_EXPIRATION or 7200)


def expires_hour():
    return timezone.now() + timedelta(hours=1)

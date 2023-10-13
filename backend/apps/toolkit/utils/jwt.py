import jwt
from django.conf import settings
from django.utils import timezone
from jwt import ExpiredSignatureError


def jwt_encode(payload, expires=None):
    payload['exp'] = timezone.now().timestamp() + (expires or settings.TOKEN_EXPIRATION or 7200)
    return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM or 'HS256')


def jwt_decode(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM or 'HS256')
        return payload, True
    except ExpiredSignatureError:
        return None, False


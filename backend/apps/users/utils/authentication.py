from django.utils import timezone
from jwt import ExpiredSignatureError
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from toolkit.utils.jwt import jwt_decode
from users.models import Token
from users.serializers.users import UserSerializer


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        payload, valid = jwt_decode(key)

        if not valid:
            raise AuthenticationFailed('Expired token.')

        token = Token.objects.select_related('user').filter(key=key).first()

        if token is None:
            raise AuthenticationFailed('Invalid or expired token.')

        if not token.user.is_active:
            raise AuthenticationFailed('User is not active or deleted.')

        if not token.is_active:
            raise AuthenticationFailed('Your token is not active.')

        return token.user, token


def sign_in_response(user, token=None, with_user_data=True, with_permissions=True):
    token = token or Token.objects.create(user=user)
    result = {'token': token.key, 'refresh': token.refresh}

    if with_user_data:
        result['user'] = UserSerializer(user).data

    if with_permissions:
        result['permissions'] = list(user.get_all_permissions())

    response = Response(result)
    response.set_cookie('refresh', token.refresh, httponly=True, samesite='strict')
    return response

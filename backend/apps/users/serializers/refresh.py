from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from toolkit.utils.serializers import BaseSerializer
from users.models import Token


class RefreshSerializer(BaseSerializer):
    refresh = serializers.SlugRelatedField('refresh', required=False, queryset=Token.objects.active())

    def validate(self, data):
        request = self.context.get('request')

        if data.get('refresh'):
            return data

        data['refresh'] = Token.objects.get_by_refresh(request.COOKIES.get('refresh'))
        print(request.COOKIES.get('refresh'))

        if not data['refresh']:
            raise ValidationError({'refresh': 'Invalid refresh token'})

        return data


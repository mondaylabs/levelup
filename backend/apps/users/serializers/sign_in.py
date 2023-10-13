from rest_framework import serializers
from django.contrib.auth import authenticate
from toolkit.utils.serializers import BaseSerializer


class SignInSerializer(BaseSerializer):
    email = serializers.EmailField(required=True, trim_whitespace=True)
    password = serializers.CharField(required=True, trim_whitespace=False)

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get('request'),
            username=attrs.get('email').lower(),  # Using email as username.
            password=attrs.get('password')
        )

        attrs['user'] = user
        return attrs

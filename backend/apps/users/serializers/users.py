from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from toolkit.utils.serializers import BaseSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        extra_kwargs = {'email': {'read_only': True}}


class SimpleUserSerializer(ModelSerializer):
    # This serializer also was used for generating JWT token.
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class ChangePasswordValidator(BaseSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)

    def validate_old_password(self, password):
        if not self.context['request'].user.check_password(password):
            raise ValidationError('Incorrect old password.')
        return password

from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from toolkit.utils.serializers import BaseSerializer
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):

    def validate_email(self, email):
        User.objects.remove_unverified(email)
        return email

    def create(self, data):
        data['email'] = data['email'].lower()
        data['username'] = data['email']  # Use email as username
        user = User.objects.create_user(**data, is_active=False)
        user.groups.add(Group.objects.get(name='admin'))  # add user to admin group
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'email': {'required': True, 'validators': [UniqueValidator(
                queryset=User.objects.unique_query(),
                message="User with this email already exists."
            )]},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }


class ConfirmationValidator(BaseSerializer):
    confirmation_code = serializers.CharField(required=True)

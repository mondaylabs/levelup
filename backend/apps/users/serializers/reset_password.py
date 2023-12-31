from rest_framework import serializers
from toolkit.utils.serializers import BaseSerializer


class GetResetLinkValidator(BaseSerializer):
    email = serializers.EmailField(required=True, write_only=True)


class ResetPasswordValidator(BaseSerializer):
    key = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8)

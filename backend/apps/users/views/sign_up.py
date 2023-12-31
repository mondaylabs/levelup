from django.db import transaction
from django.utils import timezone
from rest_framework.generics import get_object_or_404, CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView

from toolkit.views import BaseAPIView
from users.models import User
from users.serializers.sign_up import SignUpSerializer, ConfirmationValidator
from users.utils.authentication import sign_in_response
from users.utils.emails import send_verification_email


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        user = serializer.save()
        send_verification_email(self.request, user)


class ResendConfirmationEmailView(BaseAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk, verified_at=None, is_active=False)
        send_verification_email(self.request, user)
        return Response(status=200)


class ConfirmView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ConfirmationValidator

    def post(self, request):
        data = self.serializer_class.check(request)
        code = data.get('confirmation_code')
        user = get_object_or_404(User, confirmation_code=code, verified_at=None, is_active=False)
        user.verified_at = timezone.now()
        user.is_active = True
        user.save()

        return sign_in_response(user)

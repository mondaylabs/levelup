from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Token


class SignOutView(APIView):
    def delete(self, request):
        Token.objects.filter(key=request.auth.key, user=request.user).delete()
        return Response()

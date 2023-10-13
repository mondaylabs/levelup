from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from users.models import Token
from users.serializers.refresh import RefreshSerializer
from users.utils.authentication import sign_in_response


class RefreshView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RefreshSerializer

    def post(self, request):
        old_token = self.serializer_class.check(request).get('refresh')
        fresh_token = Token.objects.refresh(old_token)
        return sign_in_response(old_token.user, fresh_token, False, False)

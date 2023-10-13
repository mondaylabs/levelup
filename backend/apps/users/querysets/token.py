from toolkit.querysets.base_queryset import BaseQuerySet
from toolkit.utils.jwt import jwt_encode


class TokenQuerySet(BaseQuerySet):
    def refresh(self, old_token):
        old_token.is_active = False
        old_token.save()
        return self.create(user=old_token.user)

    def get_by_refresh(self, refresh):
        return self.filter(refresh=refresh).active().first()

    def active(self):
        return self.filter(is_active=True)

    def create(self, **kwargs):
        if 'key' not in kwargs:
            from users.serializers.users import SimpleUserSerializer
            kwargs['key'] = jwt_encode(SimpleUserSerializer(kwargs['user']).data)
        return super().create(**kwargs)


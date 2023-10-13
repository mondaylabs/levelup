from rest_framework.serializers import Serializer, ModelSerializer


class BaseSerializer(Serializer):
    @classmethod
    def check(cls, request, many=False, context=None):
        context = context or {}
        context['request'] = request
        data = request.GET if request.method == 'GET' else request.data
        serializer = cls(data=data, many=many, context=context)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class BaseModelSerializer(ModelSerializer):
    ...

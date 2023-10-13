from rest_framework.schemas.openapi import AutoSchema
from toolkit.utils.helpers import remove_prefix


class BaseSchema(AutoSchema):
    def get_tags(self, path, method):
        path = remove_prefix(path, '/api/v1/')
        tags = super().get_tags(path, method)
        return [t.capitalize() for t in tags]

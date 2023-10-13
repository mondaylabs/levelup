from django.urls import path
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

api_description = """
<h3>Authorization:</h2>
- To obtain a JWT token, use the `/api/v1/users/sign-in` endpoint.
- Pass the JWT token to the `Authorization` header using the "Token" prefix, like this: `Authorization: Token yourtokengoeshere`
- Use `/api/v1/users/refresh` endpooint to refresh your expired token.

Some private endpoints will not be visible in this documentation until you are <a href="/api-auth/login/">Signed in</a>.
"""

urlpatterns = [
    path('openapi', get_schema_view(
        title="Monday Toolkit",
        description=api_description,
        permission_classes=(AllowAny,),
        version="1.0.0"
    ), name='openapi'),
    path('', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'toolkit:openapi'}
    ), name='swagger'),
]

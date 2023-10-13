from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', RedirectView.as_view(url='/api/v1/toolkit/')),
    path('api/v1/', include([
        path('core/', include(('core.urls', 'core'))),
        path('course/', include(('course.urls', 'course'))),
        path('estimator/', include(('estimator.urls', 'estimator'))),
        path('users/', include(('users.urls', 'user'))),
        path('toolkit/', include(('toolkit.urls', 'toolkit'))),
    ])),
]

from django.urls import path

from core.views.configurations import ConfigurationsView
from core.views.general import GeneralView

urlpatterns = [
    path('configurations', ConfigurationsView.as_view()),
    path('general', GeneralView.as_view()),
]

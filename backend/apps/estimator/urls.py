from django.urls import path

from estimator.views.respondents import RespondentList

urlpatterns = [
    path('respondents', RespondentList.as_view()),
]

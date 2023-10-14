from django.urls import path

from estimator.views.respondents import RespondentList, RespondentDetail

urlpatterns = [
    path('respondents', RespondentList.as_view()),
    path('respondents/<int:pk>', RespondentDetail.as_view()),
]

from django.urls import path

from course.views.courses import CoursesList
from course.views.questions import QuestionsList

urlpatterns = [
    path('courses', CoursesList.as_view()),
    path('questions', QuestionsList.as_view()),
]

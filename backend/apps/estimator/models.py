from django.db import models
from django.db.models import CASCADE

from course.models import Course, Topic, Lesson
from toolkit.models import BaseModel
from users.models import User


class Question(BaseModel):
    text = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, CASCADE)
    lesson = models.ForeignKey(Lesson, CASCADE)

    class Meta:
        db_table = 'estimator_questions'


class Answer(BaseModel):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, CASCADE)


class Respondent(BaseModel):
    user = models.ForeignKey(User, CASCADE, null=True, blank=True)


class RespondentAnswer(BaseModel):
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, CASCADE)
    answer = models.ForeignKey(Answer, CASCADE)
    topic = models.ForeignKey(Topic, CASCADE)
    lesson = models.ForeignKey(Lesson, CASCADE)

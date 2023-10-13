from django.db import models
from django.db.models import CASCADE

from course.models import Course, Topic, Lesson
from toolkit.models import BaseModel
from users.models import User


class Question(BaseModel):
    text = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, CASCADE)
    lesson = models.ForeignKey(Lesson, CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'estimator_questions'


class Answer(BaseModel):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, CASCADE, related_name='answers')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'estimator_answers'


class Respondent(BaseModel):
    user = models.ForeignKey(User, CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'estimator_respondents'


class RespondentAnswer(BaseModel):
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, CASCADE)
    answer = models.ForeignKey(Answer, CASCADE)
    topic = models.ForeignKey(Topic, CASCADE)
    lesson = models.ForeignKey(Lesson, CASCADE)

    def __str__(self):
        return f"{self.question.text} - {self.answer.text}"

    class Meta:
        db_table = 'estimator_respondent_answers'


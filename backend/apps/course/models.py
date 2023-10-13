from django.db import models
from toolkit.models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'courses'


class Topic(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'topics'


class Lesson(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'lessons'

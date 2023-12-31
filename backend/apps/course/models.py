from django.db import models
from django.db.models import CASCADE

from toolkit.models import BaseModel


class Topic(BaseModel):
    TYPES = (
        ('hard', 'Hard skill'),
        ('soft', 'Soft skill'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPES, default='hard')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_topics'


class Lesson(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    topic = models.ForeignKey(Topic, CASCADE, related_name='lessons')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_lessons'


class Course(BaseModel):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    topics = models.ManyToManyField(Topic, related_name='courses')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_courses'

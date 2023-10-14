from rest_framework import serializers

from course.models import Course, Lesson
from toolkit.utils.serializers import BaseModelSerializer


class LessonSerializer(BaseModelSerializer):
    topic_id = serializers.IntegerField(source='topic.id')
    topic_name = serializers.CharField(source='topic.name')

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'topic_name', 'topic_id')

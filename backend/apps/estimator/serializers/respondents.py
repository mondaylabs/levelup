from django.db.models import Count, Q, FloatField
from django.db.models.functions import Cast
from rest_framework import serializers

from course.models import Lesson, Topic
from estimator.models import Respondent, RespondentAnswer
from toolkit.utils.serializers import BaseModelSerializer


class RespondentAnswerSerializer(BaseModelSerializer):
    class Meta:
        model = RespondentAnswer
        fields = ('question', 'answer')


class RespondentSerializer(BaseModelSerializer):
    respondent_answers = RespondentAnswerSerializer(many=True, write_only=True)

    def create(self, validated_data):
        respondent_answers = validated_data.pop('respondent_answers')
        instance = super().create(validated_data)

        for respondent_answer in respondent_answers:
            answer = respondent_answer.get('answer')
            question = respondent_answer.get('question')

            RespondentAnswer.objects.create(
                is_correct=answer.is_correct,
                lesson=question.lesson,
                topic=question.topic,
                respondent=instance,
                question=question,
                answer=answer,
            )

        return instance

    class Meta:
        model = Respondent
        fields = ('id', 'user', 'course', 'respondent_answers')
        extra_kwargs = {'answers': {'write_only': True}}


class RespondentDetailSerializer(BaseModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        topics = RespondentAnswer.objects\
            .values('topic__name')\
            .filter(respondent=instance)\
            .annotate(score=Cast(Count('id', filter=Q(is_correct=True)), FloatField()) / Cast(Count('id'), FloatField()))

        hard_skills = topics.filter(topic__type='hard')
        soft_skills = topics.filter(topic__type='soft')

        data['hard_skills'] = {topic['topic__name']: topic['score'] * 100 for topic in hard_skills}
        data['soft_skills'] = {topic['topic__name']: topic['score'] * 100 for topic in soft_skills}
        return data

    class Meta:
        model = Respondent
        fields = ('id', 'user')

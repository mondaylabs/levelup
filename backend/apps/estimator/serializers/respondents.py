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

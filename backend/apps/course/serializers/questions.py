from estimator.models import Question, Answer
from toolkit.utils.serializers import BaseModelSerializer


class AnswerSerializer(BaseModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text',)


class QuestionSerializer(BaseModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['answers'] = AnswerSerializer(instance.answers, many=True).data
        return data

    class Meta:
        model = Question
        fields = ('id', 'text',)

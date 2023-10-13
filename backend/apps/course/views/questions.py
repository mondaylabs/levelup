from course.serializers.questions import QuestionSerializer
from estimator.models import Question
from toolkit.views import ListMixin, BaseView


class QuestionsList(ListMixin, BaseView):
    ordering = 'id'
    filterset_fields = ('topic__course',)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

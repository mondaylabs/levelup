from course.serializers.questions import QuestionSerializer
from estimator.models import Question
from toolkit.views import ListMixin, BaseView


class QuestionsList(ListMixin, BaseView):
    ordering = 'id'
    check_retrieve_permission = False
    filterset_fields = ('topic__courses',)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

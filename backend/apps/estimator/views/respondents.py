from estimator.models import Respondent
from estimator.serializers.respondents import RespondentSerializer
from toolkit.views import CreateMixin, BaseView


class RespondentList(CreateMixin, BaseView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer

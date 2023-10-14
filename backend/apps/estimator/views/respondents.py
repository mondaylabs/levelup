from estimator.models import Respondent
from estimator.serializers.respondents import RespondentSerializer, RespondentDetailSerializer
from toolkit.views import CreateMixin, BaseView, RetrieveMixin


class RespondentList(CreateMixin, BaseView):
    check_create_permission = False
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class RespondentDetail(RetrieveMixin, BaseView):
    check_retrieve_permission = False
    queryset = Respondent.objects.all()
    serializer_class = RespondentDetailSerializer

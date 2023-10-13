from course.models import Course
from course.serializers.courses import CourseSerializer
from toolkit.views import ListMixin, BaseView


class CoursesList(ListMixin, BaseView):
    ordering = 'id'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

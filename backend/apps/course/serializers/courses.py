from course.models import Course
from toolkit.utils.serializers import BaseModelSerializer


class CourseSerializer(BaseModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name','topics','image','description')

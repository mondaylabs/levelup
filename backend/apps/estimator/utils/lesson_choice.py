from itertools import groupby
from django.forms.models import ModelChoiceField, ModelChoiceIterator

from course.models import Lesson


class LessonChoiceIterator(ModelChoiceIterator):
    def __iter__(self):
        queryset = self.queryset.select_related('topic').order_by('topic__name', 'name')
        groups = groupby(queryset, key=lambda x: x.country)
        for country, cities in groups:
            yield [
                country.name,
                [
                    (city.id, city.name)
                    for city in cities
                ]
            ]


class LessonChoiceField(ModelChoiceField):
    iterator = LessonChoiceIterator

    def __init__(self, *args, **kwargs):
        super().__init__(Lesson.objects.all(), *args, **kwargs)

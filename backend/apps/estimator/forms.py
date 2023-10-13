from django.forms import ModelForm

from course.models import Lesson, Topic


class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = []

        for topic in Topic.objects.prefetch_related('lessons'):
            options.append([
                topic.name, [[c.id, c.name] for c in topic.lessons.all()]
            ])

        self.fields["lesson"].choices = options

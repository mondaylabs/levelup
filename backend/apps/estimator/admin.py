from django.contrib import admin

from estimator.forms import QuestionForm
from estimator.models import Answer, Question
from toolkit.admin.base_admin import BaseAdmin
from toolkit.admin.mixins import AuthorMixin


class AnswerInline(admin.TabularInline):
    extra = 1
    model = Answer
    fields = ('text', 'is_correct',)


@admin.register(Question)
class QuestionAdmin(AuthorMixin, BaseAdmin):
    form = QuestionForm
    list_display = ('text', 'topic', 'lesson')
    fields = ('text', 'lesson')
    inlines = (AnswerInline,)

    def save_model(self, request, obj, form, change):
        obj.topic = obj.lesson.topic
        super().save_model(request, obj, form, change)

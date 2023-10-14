from django.contrib import admin

from course.models import Course, Topic, Lesson
from toolkit.admin.base_admin import BaseAdmin
from toolkit.admin.mixins import AuthorMixin


class LessonInline(admin.TabularInline):
    extra = 1
    model = Lesson
    fields = ('name', 'description',)


@admin.register(Topic)
class TopicAdmin(AuthorMixin, BaseAdmin):
    list_display = ('name', 'type')
    fields = ('name', 'type')
    inlines = (LessonInline,)


@admin.register(Course)
class CourseAdmin(AuthorMixin, BaseAdmin):
    list_display = ('name',)
    fields = ('name', 'topics')

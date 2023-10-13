from django.contrib import admin

from course.models import Course, Topic, Lesson
from toolkit.admin.base_admin import BaseAdmin


@admin.register(Course)
class CourseAdmin(BaseAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Topic)
class TopicAdmin(BaseAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(BaseAdmin):
    fields = ('name',)
    list_display = ('name',)

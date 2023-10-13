from django.contrib.admin.views.main import ChangeList


class AuthorMixin:
    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)


class CascadeDeleteMixin:
    def get_deleted_objects(self, objs, request):
        deleted_objects, model_count, perms_needed, protected = super().get_deleted_objects(objs, request)
        return deleted_objects, model_count, set(), protected


class DisableCreateMixin:
    def has_add_permission(self, request):
        return False


class DisableDeleteMixin:
    def has_delete_permission(self, request, obj=None):
        return False


class DisableChangeMixin:
    def has_change_permission(self, request, obj=None):
        return False


class DisableActionsMixin(DisableCreateMixin, DisableDeleteMixin, DisableChangeMixin):
    ...


class HideMixin:
    def get_model_perms(self, request):
        return {}


class ListTitleMixin:
    list_title = None

    def get_list_title(self, request):
        return self.list_title

    def changelist_view(self, request, extra_context=None):
        title = self.get_list_title(request)
        extra_context = {'title': title} if title else extra_context
        return super().changelist_view(request, extra_context=extra_context)


class UnorderedMixin:
    def get_changelist(self, request, **kwargs):
        class UnorderedChangeList(ChangeList):
            def get_ordering(self, *args, **kwargs):
                return []

        return UnorderedChangeList
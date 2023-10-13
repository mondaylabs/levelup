from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    show_full_result_count = False
    list_per_page = 100

    # set this value to `actions = ()` to enable bulk actions
    actions = None

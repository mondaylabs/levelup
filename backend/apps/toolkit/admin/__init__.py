from django.conf import settings
from django.contrib import admin

admin.site.site_header = settings.COMPANY_NAME
admin.site.index_title = 'Навигация'
admin.site.enable_nav_sidebar = False
admin.site.site_url = None
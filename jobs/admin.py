from django.contrib import admin

from .models import Job

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ['title', 'description', ('location','contract', 'schedule')]


admin.site.index_title = "GXP Admin"
admin.site.site_header = "Admin for GXP Recruitment"
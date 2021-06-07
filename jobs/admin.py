from django.contrib import admin

from .models import Contract, Job, Location, Schedule

# Register your models here.
admin.site.register(Job)
admin.site.register(Contract)
admin.site.register(Schedule)
admin.site.register(Location)

admin.site.index_title = "GXP Admin"
admin.site.site_header = "Admin for GXP Recruitment"
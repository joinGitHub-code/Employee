from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Task)

class TaskAdmin(ImportExportModelAdmin):
    pass

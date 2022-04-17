from django.contrib import admin
from result.models import Result
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Result)
class userData(ImportExportModelAdmin):
    pass
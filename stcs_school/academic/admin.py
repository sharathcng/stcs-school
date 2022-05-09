from django.contrib import admin

from academic.models import Batch, BatchClass, Subject, TeacherAllocation, Attendance, TimeTable

# Register your models here.
admin.site.register(Batch)
admin.site.register(BatchClass)
admin.site.register(Subject)
admin.site.register(TeacherAllocation)
admin.site.register(Attendance)
admin.site.register(TimeTable)
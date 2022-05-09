from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('batches',views.Batches.as_view(), name="batch"),
    path('create-new-batch', views.CreateBatch.as_view(), name="create-batch"),

    path('subjects',views.Subjects.as_view(), name="subjects"),
    path('create-new-subject', views.CreateSubject.as_view(), name="create-subject"),
    path('edit-new-subject/<int:pk>', views.UpdateSubject.as_view(), name="edit-subject"),
    path('delete-subject/<int:pk>', views.DeleteSubject.as_view(), name="delete-subject"),


    path('allClasses',views.AllClasses.as_view(), name='allClasses'),
    path('batchClasses/<str:pk>',views.BatchClasses.as_view(), name='batchClasses'),
    path('create-new-class', views.CreateClass.as_view(), name="create-class"),
    path('edit-class-details/<int:pk>', views.UpdateClassDetails.as_view(), name="edit-class-details"),

    path('teacher-allocation', views.AllocateTeacher.as_view(), name="teacher-allocation"),
    path('create-teacher-allocation', views.CreateTeacherAllocation.as_view(), name="create-teacher-allocation"),
    path('update-teacher-allocation/<int:pk>', views.UpdateTeacherAllocation.as_view(), name="update-teacher-allocation"),
    path('delete-teacher-allocation/<int:pk>', views.DeleteTeacherAllocation.as_view(), name="delete-teacher-allocation"),

    path('attendance-classes', views.AttendanceClasses.as_view(), name="attendance-classes"),
    path('attendance-dates/<int:pk>', views.AttendanceDates.as_view(), name="attendance-dates"),
    path('view-attendance/<str:pk1>', views.ViewAttendance.as_view(), name="view-attendance"),
    path('take-attendance/<str:pk>', views.TakeAttendance.as_view(), name="take-attendance"),
    path('update-old-attendance/<str:pk>', views.UpdateOldAttendance, name = "update-old-attendance"),
    path('save-attendance', views.SaveAttendance.as_view(), name="save-attendance"),

    path('upload-time-table', views.UploadTimeTable.as_view(), name="upload-time-table"),
    path('view-time-table', views.ViewTimeTable.as_view(), name="view-time-table"),
    path('update-time-table/<int:pk>', views.UpdateTimeTable.as_view(), name="update-time-table"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('dashboard', views.Dashboard.as_view(), name="dashboard"),

    path('edit-myProfile', views.UpdateTeacherMyProfile.as_view(), name="edit-teacher-myProfile"),
    path('edit-myProfile', views.UpdateStaffMyProfile.as_view(), name="edit-staff-myProfile"),
    path('edit-myProfile', views.UpdateStudentMyProfile.as_view(), name="edit-student-myProfile"),


    path('teachers', views.Teachers.as_view(), name="teachers"),
    path('create-teacher', views.CreateTeacher.as_view(), name='create-teacher'),
    path('edit-teacher-profile/<str:pk>', views.UpdateTeacherProfile.as_view(), name="edit-teacher-profile"),
    path('view-teacher-profile/<str:pk>', views.ViewTeacherProfile.as_view(), name="view-teacher-profile"),
    path('disable-teacher/<str:pk>', views.DisableTeacher.as_view(), name="disable-teacher"),
    path('enable-teacher/<str:pk>', views.EnableTeacher.as_view(), name="enable-teacher"),

    path('staffs', views.Staffs.as_view(), name="staffs"),
    path('create-staff', views.CreateStaff.as_view(), name='create-staff'),
    path('edit-staff-profile/<str:pk>', views.UpdateStaffProfile.as_view(), name="edit-staff-profile"),
    path('view-staff-profile/<str:pk>', views.ViewStaffProfile.as_view(), name="view-staff-profile"),
    path('disable-staff/<str:pk>', views.DisableStaff.as_view(), name="disable-staff"),
    path('enable-staff/<str:pk>', views.EnableStaff.as_view(), name="enable-staff"),

    path('students/<str:pk>', views.Students.as_view(), name="students"),
    path('create-student', views.CreateStudent.as_view(), name='create-student'),
    path('edit-student-profile/<str:pk>', views.UpdateStudentProfile.as_view(), name="edit-student-profile"),
    path('view-student-profile/<str:pk>', views.ViewStudentProfile.as_view(), name="view-student-profile"),
    path('disable-student/<str:pk>/<str:clsObj>', views.DisableStudent.as_view(), name="disable-student"),
    path('enable-student/<str:pk>/<str:clsObj>', views.EnableStudent.as_view(), name="enable-student"),

    path('update-parent-details/<str:pk>', views.UpdateParentDetails.as_view(), name="update-parent"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #  Home link
    path('', views.home, name='home'),

    # Admission links
    path('admission-details', views.admission, name='admission'),

    # Academics links
    path('courses-offered', views.courses, name='courses'),
    path('our-teachers', views.teachers, name='teachers'),
    path('our-teacher-details', views.teacherDetails, name='teacher-details'),

    # Events links
    path('cultural-events-details', views.cultural, name='cultural'),
    path('sports-events-details', views.sports, name='sports'),
    path('academic-events-details', views.academic, name='academic'),

    # About links
    path('about-the-school', views.about, name='about'),
    path('school-contact-details', views.contact, name='contact-us'),

    # Community links
    path('parents-details', views.parents, name='parents'),
    path('alumni-details', views.alumni, name='alumni'),

]
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "user-view/home/index.html")

# Admission
def admission(request):
    return render(request, "user-view/admission/admission.html")

# Academic views
def courses(request):
    return render(request, "user-view/academics/courses.html")

def teachers(request):
    return render(request, "user-view/academics/teachers.html")

def teacherDetails(request):
    return render(request, "user-view/academics/teacher-detail-page.html")

# Events Views
def cultural(request):
    return render(request, "user-view/events/cultural.html")

def sports(request):
    return render(request, "user-view/events/sports.html")

def academic(request):
    return render(request, "user-view/events/academic.html")

# About Views
def about(request):
    return render(request, "user-view/about/about.html")

def contact(request):
    return render(request, "user-view/about/contactUs.html")

def parents(request):
    return render(request, "user-view/community/parents.html")

def alumni(request):
    return render(request, "user-view/community/parents.html")
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import get_template

from stcs_school.settings import EMAIL_HOST_USER

# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        message_tmplt = get_template('emails/contact-form.html').render()
        adminMail = EmailMessage(
            "Feedback from " + email,
            "<h1>" + name + " wants to know about your school!<br> Please get back to them soon!</h1> <br> <p>Name: " +
            name + "<br>Email: " + email + "<br>Subject: " +
            subject + "<br>Message:" + message+"</p>",
            EMAIL_HOST_USER,
            ['cngsharath@gmail.com'],
            reply_to=['cngsharath@gmail.com']
        )
        adminMail.content_subtype = "html"
        adminMail.send()

        userMail = EmailMessage(
            "Thanks for contacting us " + name,
            message_tmplt,
            EMAIL_HOST_USER,
            [email, ],
            reply_to=[EMAIL_HOST_USER]
        )
        userMail.content_subtype = "html"
        userMail.send()
        return render(request, "user-view/home/index.html")
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

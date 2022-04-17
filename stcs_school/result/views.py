from django.shortcuts import render

from result.models import Result

# Create your views here.

def resultSearchPage(request):
    return render(request, "user-view/results/resultSearchPage.html")

def resultView(request):
    if request.method == "POST":
        regNumber = request.POST['registerNumber']
        resultObject = Result.objects.filter(userid = regNumber)
        return render(request,'user-view/results/resultPage.html', {'resultObject': resultObject})

from django.shortcuts import render

# Create your views here.
from asyncio.windows_events import NULL
from django.shortcuts import render

from result.models import Result

# Create your views here.

def resultView(request):
    if request.method == "POST":
        regNumber = request.POST['registerNumber']
        resultObject = Result.objects.filter(userid = regNumber)
        return render(request,'user-view/results/resultPage.html', {'resultObject': resultObject})

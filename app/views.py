from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.


def student(request):
    so=studentform()
    d={'so':so}
    if request.method=='POST':
        soa=studentform(request.POST)
        if soa.is_valid():
            return HttpResponse(str(soa.cleaned_data))
        else:
            return HttpResponse("data is not vaild")
    return render(request, 'student.html',d)
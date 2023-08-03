from django.shortcuts import render
from django.template import loader
# from django.http import HttpResponse
from MainApp.models import MainApp


def HomeContext(request):
    dataObjects = MainApp.objects.all().values()
    context = {
        'customerData':dataObjects
    }
    return render(request,'Home/mainFile.html',context)

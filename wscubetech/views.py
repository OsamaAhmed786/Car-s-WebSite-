from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")
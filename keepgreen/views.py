from django.shortcuts import render
from django.http import HttpResponse
from keepgreen.models import keepGreen
from django.conf import settings
import os


def home(request):
    template_path = os.path.join(settings.BASE_DIR, "templates", "index.html")
    return render(request, template_path)


def contact(request):

    return render(request, "keepgreen/index.html", contact)


def saveData(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = keepGreen(fname=fname, lname=lname, email=email, phone=phone, 
                         message=message)
        data.save()
        return HttpResponse("DATA SAVED SUCCESSFULLY")
    return render(request, "keepgreen/index.html", contact)
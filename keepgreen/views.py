from django.shortcuts import render
from django.http import HttpResponse
from keepgreen.models import keepGreen


def home(request):
    return render(request, 'index.html')


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









#def Contact(request):
    # CONTACT FORM
   # if request.method == 'POST':
       # fname = request.POST.GET('fname')
       # lname = request.POST.GET('lname')
       # email = request.POST.GET('email')
       # phone = request.POST.GET('phone')
       # message = request.POST.GET('message')
       # c = Contact(fname=fname, lname=lname, email=email, phone=phone, message=message) 
       # c.save()
       # return HttpResponse ("DATA SAVED SUCESSFULLY")
    #else:
       # return render(request, "keepgreen/index.html", contact)
        #form_data = {
         #   'fname':fname,
         #   'lname':lname,
         #   'email':email,
          #  'phone':phone,
          #  'message':message,
        #}
       # message = '''
       # From:\n\t\t{}\n
       # Message:\n\t\t{}\n
       # Email:\n\t\t{}\n
       # Phone:\n\t\t{}\n
       # '''.format(form_data['fname'],form_data['lname'], form_data['message'], form_data['email'],form_data['phone'])
        #"send_mail",('You got a mail!', message, '', ['<your_email>']) # TODO: enter your email address:

        
    #return render(request, "keepgreen/index.html", contact)
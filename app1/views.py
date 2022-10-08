from datetime import datetime
from django.shortcuts import render,HttpResponse
from app1.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

def HomePage(request):
    #messages.success(request,"this is Home Page")
    return render(request,'index.html')

def AboutPage(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email = email,phone = phone,desc = desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submitted')

    return render(request,'contact.html')
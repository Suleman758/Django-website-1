from datetime import datetime

from django.shortcuts import render,HttpResponse

from home.models import Contact
import logging
logging = logging.getLogger(__name__)

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):                  
    return render(request,'index.html')
    #return HttpResponse("this is home page") 

def about(request):
    logging.info("about page is opened")
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return HttpResponse("this is contact page")


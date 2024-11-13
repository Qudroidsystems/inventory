from http.client import HTTPResponse
from django.shortcuts import render
from .models import ContactForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

def shop(request,q):
 
  param = {'id': q}
  return render(request, 'shop.html',param)

def service(request):
  return render(request, 'services.html')


def contact(request):
  return render(request, 'contact.html')

def contactForm(request):
  return render(request, 'forms.html')

def submitForm(request):
  #checking the request type
   if request.method == 'POST':
     #getting the data from the frontend
     fn = request.POST.get('fname')
     ln = request.POST.get('lname')
     email = request.POST.get('email')
     msg = request.POST.get('message')
     print(msg)
     
     #saving data in the database via models
     cnt = ContactForm(fname=fn,lname=ln,email=email,message=msg)
     cnt.save()
     return HTTPResponse("Data saved!")
   
def contactList(request):
  all_contacts = ContactForm.objects.all
  return render(request, 'contactList.html',{'contacts': all_contacts})

     


  
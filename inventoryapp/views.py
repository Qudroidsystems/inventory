from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import ContactForm, NinModel
from django.contrib import messages


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
     #extract the data from the frontend
     fn = request.POST.get('fname')
     ln = request.POST.get('lname')
     email = request.POST.get('email')
     msg = request.POST.get('message')
 
     
     #store data in the database via models
     cnt = ContactForm(fname=fn,lname=ln,email=email,message=msg)
     saved =cnt.save()
     return HttpResponseRedirect(reverse('nin'))

     
   
def contactList(request):
  all_contacts = ContactForm.objects.all
  return render(request, 'contactList.html',{'contacts': all_contacts})

def editcontact(request):
   all_contacts = ContactForm.objects.filter(id=pk)
   return render(request, 'contactList.html')
   
   
   
   

     
def nin(request):

    if request.method == 'POST':
       check_nin= request.POST.get('nin')
       nin_exist = NinModel.objects.filter(nin=check_nin).exists()
       if nin_exist:
            messages.error(request,"NIN already exist")
            return redirect('nin')
       else:
          fullname = request.POST.get('fullname')
          nin = request.POST.get('nin')
          state = request.POST.get('state')
          nindb = NinModel(fullName = fullname,nin = nin, sor = state)
          nindb.save()
          messages.success(request,"NIN details saved")
          return redirect('nin')
    else:
        return render(request, 'nin.html')

def ninlist(request):
  all_nins = NinModel.objects.all
  return render(request, 'ninlist.html',{'nins': all_nins})

def editnin(request, ninid):
    # print(type(int(ninid)))
    person = NinModel.objects.filter(id=int(ninid))
    return render(request, 'editednin.html',{'person': person})

def updatenin(request):
      if request.method == "POST":
          fullname = request.POST.get('fullname')
          nin = request.POST.get('nin')
          state = request.POST.get('sor')
          ninid = request.POST.get('ninid')

          person = NinModel.objects.get(id=int(ninid))

          person.fulname = fullname
          person.nin = nin
          person.sor = state

          person.save()

          messages.success(request,"updated!!")
          return redirect('ninlist')

def deletenin(request,ninid):
   person = NinModel.objects.get(id=int(ninid))
   person.delete()
   messages.success(request,"removed!!")
   return redirect('ninlist')


    

  
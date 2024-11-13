from django.shortcuts import render
from .forms import FormInput


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
      if request.method == 'POST':
          form = FormInput()
          if form.is_valid():
       
              
      else:
         form = FormInput()
      return render(request, 'forms.html',{'form': form})


  
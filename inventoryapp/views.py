from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def shop(request,q):
 
  param = {'id': q}
  return render(request, 'shop.html',param)

def service(request):
  return render(request, 'services.html')
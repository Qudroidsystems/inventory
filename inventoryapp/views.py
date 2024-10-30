from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def shop(request):
  return render(request, 'shop.html')

def service(request):
  return render(request, 'services.html')
from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    path('shop/<str:q>/',views.shop),
    path('ourservice/',views.service),
    path('contact/',views.contact),
    path('form/',views.contactForm)
]

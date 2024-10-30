from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    path('shop/',views.shop),
    path('ourservice/',views.service)
]

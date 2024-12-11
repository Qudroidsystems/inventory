from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    path('shop/<str:q>/',views.shop),
    path('ourservice/',views.service),
    path('contact/',views.contact),
    path('form/',views.contactForm),
    path('submitForm/', views.submitForm),
    path('contactList/', views.contactList),
    path('nin/', views.nin,name='nin'),
    path('ninlist/', views.ninlist,name='ninlist'),
    path('editnin/<str:ninid>', views.editnin,name='editnin'),
    path('updatenin/', views.updatenin,name='updatenin'),
    path('deletenin/<str:ninid>', views.deletenin,name='deletenin'),
    path('editcontact/<str:pk>/',views.editcontact, name='editcontact')
]

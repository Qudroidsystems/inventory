from django.contrib import admin
from inventoryapp.models import BioData
from inventoryapp.models import Subject
from inventoryapp.models import ContactForm

# Register your models here.
admin.site.register(BioData)
admin.site.register(Subject)
admin.site.register(ContactForm)


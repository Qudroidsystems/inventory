from django.db import models

# Create your models here.

class BioData(models.Model):
   firstNAme = models.CharField(max_length=50)
   lastName =  models.CharField(max_length=50)
   age = models.IntegerField(max_length=100)
    

class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    subjectcode = models.CharField(max_length=50)
    biodataId = models.ForeignKey(BioData, on_delete=models.CASCADE)
    

    

   

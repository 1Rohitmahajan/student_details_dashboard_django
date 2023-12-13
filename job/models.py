from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    age=models.IntegerField(max_length=2,null=False,blank=False)
    college=models.CharField(max_length=150,null=False,blank=False)
    address=models.CharField(max_length=200,null=False,blank=False)

    def __str__(self) -> str:
        return self.name
    
class Studentidcard(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    Name=models.CharField(null=False,max_length=100,blank=False)
    prn=models.IntegerField(null=False,max_length=14,blank=False)
    age=models.IntegerField(null=False,max_length=3,blank=False)
    birth=models.DateField(null=False,blank=False)
    phone=models.IntegerField(null=False,max_length=12,blank=False)
    address=models.CharField(null=False,max_length=150,blank=False)
    field=models.CharField(null=False,blank=False,max_length=100)
    college=models.CharField(null=False,blank=False,max_length=150)
    study=models.BooleanField(default=False)
    
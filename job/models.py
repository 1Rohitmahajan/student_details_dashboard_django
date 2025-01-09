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
    
class Author(models.Model):
    gender_choices=(("male","male"),("female","female"))
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=50, choices=gender_choices,default="male")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.RESTRICT)
    publisher=models.ForeignKey(Publisher,on_delete=models.RESTRICT)
    price=models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)  # Many-to-Many relationship
    img=models.ImageField(blank=True,null=True,upload_to="book_img/" ,)
    file=models.FileField(upload_to="file/",default='default_file.txt')


    def __str__(self):
        return self.title
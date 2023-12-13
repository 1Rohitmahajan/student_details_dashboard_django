from django.contrib import admin
from django.urls import path
from job import views



urlpatterns = [
   path('', views.home, name="home"),
   path('home', views.home, name="home"),


   path('index', views.index, name="index"),
   path('student',views.student,name='student'),
   path('student_details',views.student_details,name="student_details"),
   path('studentidcard',views.studentidcard,name='studentidcard')

]
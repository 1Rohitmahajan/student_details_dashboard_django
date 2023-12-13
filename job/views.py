from django.shortcuts import render

from django.http import HttpResponse
from job.models import Student
def index(request):
    return render(request,'index.html')

def home(request):
    check=False
    name='dj'
    if request.method=='POST':
        name=request.POST['name']
        check=request.POST.get('ch')
        print(name)
        print(check)
    isactive=True
    list_of_program=["wap","prime number",
                     "palindrom number","circle radius"]
    
    student={
        'student_name':"rohit",
        'student_college':"imrd",
        'student_city':"jalgaon"
    }
    data={
        'isactive':isactive,
        'list_of_program':list_of_program,
        'student':student,
        'name':name,
        'check':check
        
        
    }
    return render(request,"home.html",data)

def student(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        address=request.POST.get("address")
        college=request.POST.get("college")

        studentinfo=Student(name=name,age=age,address=address,college=college)

        studentinfo.save()


    return render(request,"student.html")

def student_details(request):
    p=Student.objects.all()

    data={
        'p':p
    }
    return render(request,'student_details.html',data)
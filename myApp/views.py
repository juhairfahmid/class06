from django.shortcuts import render,redirect
from .models import *


def studentPage(request):
    
    student = Student_M.objects.all()
    
    context = {
        'stu' : student, 
    }
    
    return render(request,'student/index.html',context)

def studentAdd(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        sclass = request.POST.get("class")
        roll = request.POST.get("roll")
        bgroup = request.POST.get("bgroup")
        
        student = Student_M(
            Student_Name = name,
            Student_Class = sclass,
            Student_Roll = roll,
            Student_Bgroup = bgroup,
        )
    
        student.save()
        
        return redirect("studentPage")
    
    return render(request,"student/addstudent.html")

def studentEdit(request):
    
    if request.method == "POST" :
        stu_id = request.POST.get("student_id")
        name = request.POST.get("name")
        sclass = request.POST.get("class")
        roll = request.POST.get("roll")
        bgroup = request.POST.get("bgroup")
        
        student = Student_M(
            id= stu_id, 
            Student_Name = name,
            Student_Class = sclass,
            Student_Roll = roll,
            Student_Bgroup = bgroup,
        )
        
        student.save()
        
        return redirect("studentPage")
    
    

    
    

def studentIdCall(request,myid):
    studentid = Student_M.objects.filter(id=myid)
    return render(request,"student/editstudent.html", {'stu':studentid})




def teacherPage(request):
    
    teacher = Teacher_M.objects.all()
    
    context = {
        'teach' : teacher,
    }
    return render(request,'teacher/index.html', context)

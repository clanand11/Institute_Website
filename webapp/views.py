from django.shortcuts import render,redirect, get_object_or_404
from .forms import CourseForm
from django.http import HttpResponseRedirect
from .models import Course
from django.contrib import messages

def home(request):
    return render(request,'webapp/home.html')

def gallery(request):
    return render(request,'webapp/gallery.html')

def courses(request):
    courseList=Course.objects.all().order_by('name')
    return render(request, 'webapp/courses.html',{'courseList':courseList})

def searchCourse(request):
    if request.method == "POST":
        searched=request.POST["searched"]
        courses=Course.objects.filter(name__contains=searched)
        return render(request, 'webapp/searchCourse.html',{'searched':searched, 'courses':courses})
    else:   	
        return render(request, 'webapp/searchCourse.html',{})
    
def updateCourse(request,course_id):
    course=Course.objects.get(pk=course_id)
    form=CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('coursesPage')
    return render(request,'webapp/courseUpdate.html',{'form':form })

def addCourse(request):
    submitted=False
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            submitted=True
            return render(request,'webapp/addCourse.html',{'form':form, 'submitted':submitted})
    else:
        form=CourseForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'webapp/addCourse.html',{'form':form, 'submitted':submitted})

def deleteCourse(request,course_id):
    if request.user.is_superuser:
        course=Course.objects.get(pk=course_id)
        course.delete()
        messages.success(request, "Event Deleted !!")
        return redirect('coursesPage')
    else:
        messages.success(request, 'You are not authorised to delete')
        return redirect('coursesPage')
    
def registerCourse(request,course_id):
    if request.user.is_authenticated:
        course=get_object_or_404(Course, id=course_id)
        request.user.courses.add(course)
        request.user.save()
    return redirect('coursesPage')

def viewStudents(request,course_id):
    if request.user.is_superuser:
        course=Course.objects.get(id=course_id)
        students=course.customuser_set.all()
    return render(request, 'webapp/viewstudents.html',{'students':students ,'course':course.name})
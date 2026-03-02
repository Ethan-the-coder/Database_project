from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from Dashboard.models import Student

# Create your views here.
@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        date = request.POST.get('date')

        Student.objects.create(
            image=image,
            name=name,
            course=course,
            age=age,
            gender=gender,
            email=email,
            date=date )
        return redirect('dashboard')
    return render(request, 'add_student.html')

def update_student(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        if request.FILES.get('image'):
            student.image = request.FILES.get('image')
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')
        student.date = request.POST.get('date')
        student.save()
        return redirect('dashboard')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        student.save()
        return redirect('dashboard')
    student.delete()
    return redirect('dashboard')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
            return redirect('signup')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('dashboard')
    return render(request, 'sign_up.html')








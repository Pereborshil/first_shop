from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Course, Category
from .forms import RegistrationForm



def index(request):
    courses = Course.objects.all()
    return render(request,'shop/courses.html', {'courses':courses})

def single_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404()


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'shop/registration.html', {'form': form})
    
    
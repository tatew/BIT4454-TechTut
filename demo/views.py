from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def index(request):
    students = Student.objects.order_by('name')

    context = {
        'students': students
    }

    return render(request, 'demo/hello.html', context)
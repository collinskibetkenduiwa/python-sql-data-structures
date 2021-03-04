from django.shortcuts import render
from .models import Book
# from django.http import HttpResponse


# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,'reading/index.html',{'books':books})
    
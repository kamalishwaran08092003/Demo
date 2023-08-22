from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Newapp
from django.http import HttpResponseRedirect
from django.urls import reverse

def book(request):
    Book = Newapp.objects.all()
    template = loader.get_template('book.html')
    context = {
        'Book' : Book
    }
    return HttpResponse(template.render(context, request))

    
def index1(request):
    s1=student.objects.all()
    return render(request,'student.html',{'s1':s1})


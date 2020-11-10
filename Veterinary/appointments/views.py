from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
#from .models import Question,Choice
from django.http import Http404
from django.urls import reverse

def home(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context={}
    return render(request, 'appointments/home.html', context)

def about(request):
    context={}
    return render(request, 'appointments/about.html', context)

def services(request):
    context={}
    return render(request, 'appointments/services.html', context)

def log(request):
    context={}
    return render(request, 'appointments/log.html', context)

def contact(request):
    context={}
    return render(request, 'appointments/contact.html', context)
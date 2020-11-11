from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import *


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
    new_form = AppForm()
    note = ''
    context={
        'note': note,
        'appform': new_form
    }
    return render(request, 'appointments/log.html', context)

def contact(request):
    context={}
    return render(request, 'appointments/contact.html', context)


def confirm(request):
    context={}
    return render(request, 'appointments/confirm.html', context)
    
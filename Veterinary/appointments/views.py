from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import *


def home(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    context={
        'username': username,
    }
    return render(request, 'appointments/home.html', context)

def about(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    context={
        'username': username,
    }
    return render(request, 'appointments/about.html', context)

def services(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    context={
        'username': username,
    }
    return render(request, 'appointments/services.html', context)

def app(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    if username=='':
        userlogform=UserLogForm()
        context={
            'username': username,
            'userlogform': userlogform,
            'note':'',
        }
        return render(request,'appointments/login.html',context)
    else:
        new_app_form = AppForm()
        new_pet_form = PetForm()
        note = ''
        context={
            'note': note,
            'appform': new_app_form,
            'petform': new_pet_form,
            'username': username,
        }
        return render(request, 'appointments/summary.html', context)

def contact(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    context={
        'username': username,
    }
    return render(request, 'appointments/contact.html', context)


def confirm(request):
    new_app_form=AppForm()
    new_pet_form=PetForm()
    uname=request.session['username']
    if request.method=='POST':
        filled_app_form=AppForm(request.POST,prefix='appform')
        filled_pet_form=PetForm(request.POST,prefix="petform")

        if filled_app_form.is_valid() and filled_pet_form.is_valid():
            l_client=Client.objects.get(username=uname)         # FIXME to use current user
            l_vet=filled_app_form.cleaned_data.get("veterinary")
            l_date=filled_app_form.cleaned_data.get("date")
            l_time=filled_app_form.cleaned_data.get("time")
            l_pet=filled_app_form.cleaned_data.get("pet")       # FIXME check del pet
            l_reason=filled_app_form.cleaned_data.get("reason")
            l_req_date=timezone.now()



            app_det=Appointments(
                client=l_client,
                veterinary=l_vet,
                date=l_date,
                time=l_time,
                pet=l_pet,
                reason=l_reason,
                req_date=l_req_date
            )
            app_det.save()

            note="Appointment confirmed"
            context = {
                'note': note,
            }
            return HttpResponseRedirect(reverse('appointments:summary'))

        else:
            note="Incorrect values, try again"
            context = {
                'note': note,
                'appform': filled_app_form,
                'petform': filled_pet_form,
            }
            return render(request,'appointments/app.html',context)

    else:
        note="Incorrect values, try again"
        context = {
            'note': note,
            'appform': new_app_form,
            'petform': new_pet_form,
        }
        return render(request,'appointments/app.html',context)
    
def summary(request):
    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    
    note="Your appointments"
    context = {
        'note': note,
        'username': username,
    }
    return render(request,'appointments/summary.html',context)

def login(request):
    username=''
    userlogform=UserLogForm()
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    context={
        'username': username,
        'userlogform': userlogform,
        'note':'',
    }
    return render(request,'appointments/login.html',context)

def logout(request):
    request.session['username']=''
    
    context={
        'username': '',
    }
    return render(request,'appointments/home.html',context)

def checklog(request):
    new_form = UserLogForm()
    if request.method=='POST':
        filled_form=UserLogForm(request.POST)
        
        if filled_form.is_valid():
            # Check if admin or client
            uname=filled_form.cleaned_data.get('username')
            pwd=filled_form.cleaned_data.get('password')

            # Is client
            qs_c=Client.objects.filter(username=uname)
            qs_v=Veterinary.objects.filter(username=uname)
            if qs_c.count() > 0:
                # check password
                if qs_c[0].password==pwd:
                    request.session['username']=qs_c[0].name
                    return HttpResponseRedirect(reverse('appointments:summary'))
                else:
                    context={
                        'username': '',
                        'userlogform': new_form,
                        'note':'Wrong password',
                    }
                    return render(request,'appointments/login.html',context)
            
            # Is Vet
            elif qs_v.count() > 0:
                # check password
                if qs_v[0].password==pwd:
                    request.session['username']=qs_v[0].name
                    return HttpResponseRedirect(reverse('appointments:summary'))
                else:
                    context={
                        'username': '',
                        'userlogform': new_form,
                        'note':'Wrong password',
                    }
                    return render(request,'appointments/login.html',context)
            # Not registered
            else:
                context={
                    'username': '',
                    'userlogform': new_form,
                    'note':'Not registered',
                }
                return render(request,'appointments/login.html',context)

        else:
            context={
                'username': '',
                'userlogform': new_form,
                'note':'Wrong credentials or not registered',
            }
            return render(request,'appointments/login.html',context)
    else:
        context={
            'username': '',
            'userlogform': new_form,
            'note':'Wrong credentials or not registered',
        }
        return render(request,'appointments/login.html',context)
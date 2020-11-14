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
        context={
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
            l_client=Client.objects.get(username=uname)         
            l_vet=filled_app_form.cleaned_data.get("veterinary")
            l_date=filled_app_form.cleaned_data.get("date")
            l_time=filled_app_form.cleaned_data.get("time")
            l_reason=filled_app_form.cleaned_data.get("reason")
            l_req_date=timezone.now()

            pet_name=filled_pet_form.cleaned_data.get("name")

            pet_match=Pet.objects.filter(name=pet_name).filter(owner=l_client)
            if pet_match.count()==1:
                l_pet=pet_match[0]
            else:
                l_pet=Pet(
                    owner=l_client,
                    name=filled_pet_form.cleaned_data.get("name"),
                    gender=filled_pet_form.cleaned_data.get("gender"),
                    age=filled_pet_form.cleaned_data.get("age"),
                    species=filled_pet_form.cleaned_data.get("species"),
                )
                l_pet.save()



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
    username=request.session['username']
    
    note="Your appointments"
    context = {
        'note': note,
        'username': username,
    }
    return render(request,'appointments/summary.html',context)

def login(request):
    username=''
    userlogform=UserLogForm()
    
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
                    return HttpResponseRedirect(reverse('appointments:adminsum'))
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

def usernewapp(request):
    username=request.session['username']
    
    new_app_form = AppForm()
    new_pet_form = PetForm()
    context={
        'note': '',
        'appform': new_app_form,
        'petform': new_pet_form,
        'username': username,
    }
    return render(request, 'appointments/app.html', context)

def adminsum(request):
    username=request.session['username']
    
    context={
        'username': username,
    }
    return render(request, 'appointments/adminsum.html', context)

def reguser(request):
    username=''
    userregform=UserRegForm()
    context={
        'username': username,
        'userregform':userregform,
    }
    return render(request, 'appointments/userreg.html', context)

def regadmin(request):
    username=''
    adminregform=AdminRegForm()
    context={
        'username': username,
        'adminregform':adminregform,
    }
    return render(request, 'appointments/adminreg.html', context)

def checkadminreg(request):
    if request.method=='POST':
        filled_form=AdminRegForm(request.POST)
        
        if filled_form.is_valid():
            # Check username
            uname=filled_form.cleaned_data.get("username")
            admin_pwd=filled_form.cleaned_data.get("admin_pwd")
            
            if Veterinary.objects.filter(username=uname).count()==0:
                # Check secret admin password
                if admin_pwd=='secret':
                    # Save admin
                    request.session['username']=uname
                    new_admin=Veterinary(
                        username=uname,
                        name=filled_form.cleaned_data.get("name"),
                        email=filled_form.cleaned_data.get("email"),
                        password=filled_form.cleaned_data.get("password"),
                        telephone=filled_form.cleaned_data.get("telephone"),
                    )
                    new_admin.save()
                    context={
                        'username':uname,
                    }
                    return HttpResponseRedirect(reverse('appointments:adminsum'))

                else:
                    context={
                        'note': 'Wrong admin password',
                        'adminregform':filled_form,
                        'username': '',
                    }
                    return render(request, 'appointments/adminreg.html', context)    
            # Already taken username
            else:
                context={
                    'note': 'Username '+uname+' already taken',
                    'adminregform':filled_form,
                    'username': '',
                }
                return render(request, 'appointments/adminreg.html', context)
        else:
            context={
                'note': '',
                'adminregform':filled_form,
                'username': 'Wrong information',
            }
            return render(request, 'appointments/adminreg.html', context)    

    else:
        context={
            'note': '',
            'adminregform':filled_form,
            'username': 'Wrong information',
        }
        return render(request, 'appointments/adminreg.html', context)


def checkuserreg(request):
    if request.method=='POST':
        filled_form=UserRegForm(request.POST)
        
        if filled_form.is_valid():
            # Check username
            uname=filled_form.cleaned_data.get("username")
            
            if Client.objects.filter(username=uname).count()==0:
                
                # Save user
                request.session['username']=uname
                new_user=Client(
                    username=uname,
                    name=filled_form.cleaned_data.get("name"),
                    email=filled_form.cleaned_data.get("email"),
                    password=filled_form.cleaned_data.get("password"),
                    telephone=filled_form.cleaned_data.get("telephone"),
                )
                new_user.save()
                context={
                    'username':uname,
                }
                return HttpResponseRedirect(reverse('appointments:summary'))
 
            # Already taken username
            else:
                context={
                    'note': 'Username '+uname+' already taken',
                    'userregform':filled_form,
                    'username': '',
                }
                return render(request, 'appointments/userreg.html', context)
        else:
            context={
                'note': '',
                'userregform':filled_form,
                'username': 'Wrong information',
            }
            return render(request, 'appointments/userreg.html', context)    

    else:
        context={
            'note': '',
            'userregform':filled_form,
            'username': 'Wrong information',
        }
        return render(request, 'appointments/userreg.html', context)
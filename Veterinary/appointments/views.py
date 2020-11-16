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
        uname=request.session['username']
        client_object=Client.objects.get(username=uname)
        user_apps=Appointments.objects.filter(client=client_object).order_by('date')

        
        if user_apps.count()>0:
            has_apps=True
        else:
            has_apps=False
        
        note="Your appointments"
        context = {
            'note': note,
            'username': uname,
            'user_apps':user_apps,
            'has_apps':has_apps,
        }
        return render(request,'appointments/summary.html',context)

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
    
def adminconfirm(request):
    new_app_form=AdminAppForm()
    new_pet_form=PetForm()
    #uname=request.session['username']
    if request.method=='POST':
        filled_app_form=AdminAppForm(request.POST,prefix='appform')
        filled_pet_form=PetForm(request.POST,prefix="petform")

        if filled_app_form.is_valid() and filled_pet_form.is_valid():
            l_client=filled_app_form.cleaned_data.get("client")
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
            return HttpResponseRedirect(reverse('appointments:adminsum'))
            
        else:
            note="Incorrect values, try again"
            context = {
                'note': note,
                'appform': filled_app_form,
                'petform': filled_pet_form,
            }
            return render(request,'appointments/adminnewapp.html',context)

    else:
        note="Incorrect values, try again"
        context = {
            'note': note,
            'appform': new_app_form,
            'petform': new_pet_form,
        }
        return render(request,'appointments/adminnewapp.html',context)

def summary(request):
    uname=request.session['username']
    client_object=Client.objects.get(username=uname)
    user_apps=Appointments.objects.filter(client=client_object).order_by('date')

    if user_apps.count()>0:
        has_apps=True
    else:
        has_apps=False
    
    note="Your appointments"
    context = {
        'note': note,
        'username': uname,
        'user_apps':user_apps,
        'has_apps':has_apps,
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
    request.session['is_vet']=False
    
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
                    request.session['is_vet']=False
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
                    request.session['is_vet']=True
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
    uname=request.session['username']
    user_apps=Appointments.objects.order_by('date')

    if user_apps.count()>0:
        has_apps=True
    else:
        has_apps=False
    
    context = {
        'username': uname,
        'user_apps':user_apps,
        'has_apps':has_apps,
    }
    return render(request,'appointments/adminsum.html',context)

def adminpetsum(request):
    uname=request.session['username']
    pets=Pet.objects.all()

    if pets.count()>0:
        has_pets=True
    else:
        has_pets=False
    
    context = {
        'username': uname,
        'pets':pets,
        'has_pets':has_pets,
    }
    return render(request,'appointments/adminpetsum.html',context)

def adminusersum(request):
    uname=request.session['username']
    users=Client.objects.all()

    if users.count()>0:
        has_users=True
    else:
        has_users=False
    
    context = {
        'username': uname,
        'users':users,
        'has_users':has_users,
    }
    return render(request,'appointments/adminusersum.html',context)

def adminvetsum(request):
    uname=request.session['username']
    vets=Veterinary.objects.all()

    if vets.count()>0:
        has_vets=True
    else:
        has_vets=False
    
    context = {
        'username': uname,
        'vets':vets,
        'has_vets':has_vets,
    }
    return render(request,'appointments/adminvetsum.html',context)

def reguser(request):
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''
    
    userregform=UserRegForm()
    context={
        'username': username,
        'userregform':userregform,
        'is_vet':is_vet,
    }
    return render(request, 'appointments/userreg.html', context)

def regadmin(request):
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''

    adminregform=AdminRegForm()
    context={
        'username': username,
        'adminregform':adminregform,
        'is_vet':is_vet,
    }
    return render(request, 'appointments/adminreg.html', context)

def checkadminreg(request,object_id=None):
    if object_id is not None:
        Veterinary.objects.filter(id=object_id).delete()
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    
    username=request.session['username']

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
                    if not is_vet:
                        request.session['username']=uname
                        request.session['is_vet']=True
                    new_admin=Veterinary(
                        username=uname,
                        name=filled_form.cleaned_data.get("name"),
                        email=filled_form.cleaned_data.get("email"),
                        password=filled_form.cleaned_data.get("password"),
                        telephone=filled_form.cleaned_data.get("telephone"),
                    )
                    new_admin.save()
                    context={
                        'username':request.session['is_vet'],
                    }
                    if not is_vet:
                        return HttpResponseRedirect(reverse('appointments:adminsum'))
                    else:
                        return HttpResponseRedirect(reverse('appointments:adminvetsum'))

                else:
                    context={
                        'note': 'Wrong admin password',
                        'adminregform':filled_form,
                        'username': request.session['username'],
                    }
                    
                    if not is_vet:                    
                        return render(request, 'appointments/adminreg.html', context)
                    else:
                        return render(request, 'appointments/adminadminreg.html', context)
            # Already taken username
            else:
                context={
                    'note': 'Username '+uname+' already taken',
                    'adminregform':filled_form,
                    'username': request.session['username'],
                }
                if not is_vet:                    
                    return render(request, 'appointments/adminreg.html', context)
                else:
                    return render(request, 'appointments/adminadminreg.html', context)
        else:
            context={
                'note': 'Wrong information',
                'adminregform':filled_form,
                'username': request.session['username'],
            }
            if not is_vet:                    
                return render(request, 'appointments/adminreg.html', context)
            else:
                return render(request, 'appointments/adminadminreg.html', context)   

    else:
        context={
            'note': 'Wrong information',
            'adminregform':filled_form,
            'username': request.session['username'],
        }
        if not is_vet:                    
            return render(request, 'appointments/adminreg.html', context)
        else:
            return render(request, 'appointments/adminadminreg.html', context)


def checkuserreg(request,object_id=None):
    if object_id is not None:
        Client.objects.filter(id=object_id).delete()

    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    
    username=request.session['username']
    
    if request.method=='POST':
        filled_form=UserRegForm(request.POST)
        
        if filled_form.is_valid():
            # Check username
            uname=filled_form.cleaned_data.get("username")
            
            if Client.objects.filter(username=uname).count()==0:
                
                # Save user
                if not is_vet:                    
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
                    'username':request.session['username'],
                }
                if not is_vet:
                    return HttpResponseRedirect(reverse('appointments:summary'))
                else:
                    return HttpResponseRedirect(reverse('appointments:adminusersum'))
            # Already taken username
            else:
                context={
                    'note': 'Username '+uname+' already taken',
                    'userregform':filled_form,
                    'username': '',
                }
                if not is_vet:                    
                    return render(request, 'appointments/userreg.html', context)
                else:
                    return render(request, 'appointments/adminuserreg.html', context)
        else:
            context={
                'note': 'Wrong information',
                'userregform':filled_form,
                'username': request.session['username'],
            }
            if not is_vet:                    
                return render(request, 'appointments/userreg.html', context)
            else:
                return render(request, 'appointments/adminuserreg.html', context) 

    else:
        context={
            'note': 'Wrong information',
            'userregform':filled_form,
            'username': request.session['username'],
        }
        if not is_vet:                    
            return render(request, 'appointments/userreg.html', context)
        else:
            return render(request, 'appointments/adminuserreg.html', context)

def userdelapp(request,question_id):
    appointment=Appointments.objects.filter(id=question_id)
    appointment.delete()

    uname=request.session['username']
    client_object=Client.objects.get(username=uname)
    user_apps=Appointments.objects.filter(client=client_object).order_by('date')

    if user_apps.count()>0:
        has_apps=True
    else:
        has_apps=False
    
    context = {
        'username': uname,
        'user_apps':user_apps,
        'has_apps':has_apps,
    }
    return render(request,'appointments/summary.html',context)

def usermodapp(request,question_id): 
    uname=request.session['username']
    app=Appointments.objects.filter(id=question_id)[0]

    filled_pet_form=PetForm(initial={
        'name':app.pet.name,
        'gender':app.pet.gender,
        'age':app.pet.age,
        'species':app.pet.species,
    })
    filled_app_form=AppForm(initial={
        'veterinary':app.veterinary,
        'date':app.date,
        'time':app.time,
        'reason':app.reason,
    })

    context = {
        'username': uname,
        'question_id':question_id,
        'appform':filled_app_form,
        'petform':filled_pet_form,
    }
    return render(request,'appointments/usermod.html',context)

def usersavechanges(request,question_id):
    app=Appointments.objects.filter(id=question_id)
    app.delete()
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

def admindelapp(request,question_id):
    appointment=Appointments.objects.filter(id=question_id)
    appointment.delete()

    uname=request.session['username']
    user_apps=Appointments.objects.order_by('date')

    if user_apps.count()>0:
        has_apps=True
    else:
        has_apps=False
    
    context = {
        'username': uname,
        'user_apps':user_apps,
        'has_apps':has_apps,
    }
    return render(request,'appointments/adminsum.html',context)

def adminmodapp(request,question_id): 
    uname=request.session['username']
    app=Appointments.objects.filter(id=question_id)[0]

    filled_pet_form=PetForm(initial={
        'name':app.pet.name,
        'gender':app.pet.gender,
        'age':app.pet.age,
        'species':app.pet.species,
    })
    filled_app_form=AppForm(initial={
        'veterinary':app.veterinary,
        'date':app.date,
        'time':app.time,
        'reason':app.reason,
    })

    context = {
        'username': uname,
        'question_id':question_id,
        'appform':filled_app_form,
        'petform':filled_pet_form,
    }
    return render(request,'appointments/adminmodapp.html',context)

def adminsavechanges(request,question_id):
    app=Appointments.objects.filter(id=question_id)
    client_uname=app[0].client.username
    app.delete()
    
    new_app_form=AppForm()
    new_pet_form=PetForm()
    uname=request.session['username']
    
    if request.method=='POST':
        filled_app_form=AppForm(request.POST,prefix='appform')
        filled_pet_form=PetForm(request.POST,prefix="petform")

        if filled_app_form.is_valid() and filled_pet_form.is_valid():
            l_client=Client.objects.get(username=client_uname)         
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

            context = {
                'uname':uname,
            }
            return HttpResponseRedirect(reverse('appointments:adminsum'))

        else:
            note="Incorrect values, try again"
            context = {
                'note': note,
                'appform': filled_app_form,
                'petform': filled_pet_form,
            }
            return render(request,'appointments/adminnewapp.html',context)

    else:
        note="Incorrect values, try again"
        context = {
            'note': note,
            'appform': new_app_form,
            'petform': new_pet_form,
        }
        return render(request,'appointments/adminnewapp.html',context)

def adminnewapp(request):
    username=request.session['username']
    
    new_app_form = AdminAppForm()
    new_pet_form = PetForm()
    context={
        'note': '',
        'adminappform': new_app_form,
        'petform': new_pet_form,
        'username': username,
    }
    return render(request, 'appointments/adminnewapp.html', context)

def adminadminreg(request):
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''

    adminregform=AdminRegForm()
    context={
        'username': username,
        'adminregform':adminregform,
        'is_vet':is_vet,
    }
    return render(request, 'appointments/adminadminreg.html', context)

def adminuserreg(request):
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=''
    try:
        username=request.session['username']
    except KeyError:
        request.session['username']=''

    userregform=UserRegForm()
    context={
        'username': username,
        'userregform':userregform,
        'is_vet':is_vet,
    }
    return render(request, 'appointments/adminuserreg.html', context)

def adminpetreg(request):

    username=request.session['username']
    
    adminpetform=AdminPetForm()
    context={
        'username': username,
        'adminpetform':adminpetform,
    }
    return render(request, 'appointments/adminpetreg.html', context)

def checkpetreg(request,object_id=None):
    if object_id is not None:
        Pet.objects.filter(id=object_id).delete()

    filled_form=AdminPetForm(request.POST)
    username=request.session['username']
    
    if request.method=='POST':
        if filled_form.is_valid():
            filled_form.save()
            pets=Pet.objects.all()

            if pets.count()>0:
                has_pets=True
            else:
                has_pets=False
            
            context = {
                'username': username,
                'pets':pets,
                'has_pets':has_pets,
            }
            return render(request,'appointments/adminpetsum.html',context)
        else:
            context={
            'username': username,
            'adminpetform':filled_form,
            'note': 'Wrong information, try again',
        }
        return render(request, 'appointments/adminpetreg.html', context)

    else:
    
        context={
            'username': username,
            'adminpetform':filled_form,
            'note': 'Wrong information, try again',
        }
        return render(request, 'appointments/adminpetreg.html', context)

def admindeluser(request,object_id):
    Client.objects.filter(id=object_id).delete()
    
    uname=request.session['username']
    users=Client.objects.all()

    if users.count()>0:
        has_users=True
    else:
        has_users=False
    
    context = {
        'username': uname,
        'users':users,
        'has_users':has_users,
    }
    return render(request,'appointments/adminusersum.html',context)

def admindeladmin(request,object_id):
    Veterinary.objects.filter(id=object_id).delete()
    uname=request.session['username']
    vets=Veterinary.objects.all()

    if vets.count()>0:
        has_vets=True
    else:
        has_vets=False
    
    context = {
        'username': uname,
        'vets':vets,
        'has_vets':has_vets,
    }
    return render(request,'appointments/adminvetsum.html',context)

def admindelpet(request,object_id):
    Pet.objects.filter(id=object_id).delete()
    uname=request.session['username']
    pets=Pet.objects.all()

    if pets.count()>0:
        has_pets=True
    else:
        has_pets=False
    
    context = {
        'username': uname,
        'pets':pets,
        'has_pets':has_pets,
    }
    return render(request,'appointments/adminpetsum.html',context)

def adminmoduser(request,object_id): 
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=request.session['username']
    client=Client.objects.filter(id=object_id)[0]

    userregform=UserRegForm(initial={
        'username':client.username,
        'name':client.name,
        'email':client.email,
        'password':client.password,
        'telephone':client.telephone,
    })
    

    context={
        'username': username,
        'userregform':userregform,
        'is_vet':is_vet,
        'object_id':object_id,
    }
    return render(request, 'appointments/adminuserreg.html', context)

def adminmodadmin(request,object_id): 
    try:
        is_vet=request.session['is_vet']
    except KeyError:
        is_vet=False

    username=request.session['username']
    vet=Veterinary.objects.filter(id=object_id)[0]

    adminregform=UserRegForm(initial={
        'username':vet.username,
        'name':vet.name,
        'email':vet.email,
        'password':vet.password,
        'telephone':vet.telephone,
    })
    

    context={
        'username': username,
        'adminregform':adminregform,
        'is_vet':is_vet,
        'object_id':object_id,
    }
    return render(request, 'appointments/adminadminreg.html', context)

def adminmodpet(request,object_id): 
    
    username=request.session['username']
    pet=Pet.objects.filter(id=object_id)[0]

    adminpetform=AdminPetForm(initial={
        'owner':pet.owner,
        'name':pet.name,
        'gender':pet.gender,
        'age':pet.age,
        'species':pet.species,
    })
    
    context={
        'username': username,
        'adminpetform':adminpetform,
        'object_id':object_id
    }
    return render(request, 'appointments/adminpetreg.html', context)
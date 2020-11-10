from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm, NewAdminForm

# Create your views here.
def register_admin(request):
    if request.method == 'POST':
        form = NewAdminForm(request.POST)
        request.user.is_staff = True
        if form.is_valid():
            form.save()
            return redirect('/account')
        args = {'form':form}
        return render(request, 'accounts/admin_form.html',args)
    else: #User requests empty form
        form = RegisterForm()

        args = {'form':form}
        return render(request, 'accounts/admin_form.html',args)

def home(request):
    if request.user.is_authenticated:
        return render(request,'accounts/home.html')
    else:
        return redirect('/account/login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
        args = {'form':form}
        return render(request, 'accounts/reg_form.html',args)
    else: #User requests empty form
        form = RegisterForm()

        args = {'form':form}
        return render(request, 'accounts/reg_form.html',args)


def profile(request):
    if request.user.is_authenticated: 
        args = {'user':request.user}
        return render(request,'accounts/profile.html',args)
    else:
        return redirect('/account/login')
    
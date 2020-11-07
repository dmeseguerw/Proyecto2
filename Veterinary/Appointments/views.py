from django.http import HttpResponse, Http404
from .models import Pet
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

# Create your views here.
def init(request):
    return render(request, "init.html")
    
def home(request):
    return render(request, "home.html")

def new(request):
    return HttpResponse('Showing "new" page')

def delete(request):
    return HttpResponse('Showing "delete" page')

def check(request,pk=None):
    if pk is not None:
        try:
            pet = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404('Pet with pk {} doesn\'t exist.', format(pk))
        return render(request,'check.html',{
            'object_pk': pet.pk,
            'object_name': pet.name,
            'object_age': pet.age,
        },)
    
    else:

        pet_dict = {}
        for pet in Pet.objects.all():
            pet_dict[pet.name] = {
                'pk': pet.pk,
                'age': pet.age,
            }

        return render(request,'check.html',{'pet_dict':pet_dict},)
    # return HttpResponse('Showing "check" page')
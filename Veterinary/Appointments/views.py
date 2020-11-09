from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet


# Create your views here.

def home(request):
    return HttpResponse('Showing "home" page')

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
from django.shortcuts import render
from .models import Student
from .forms import StudentForm
 # create view
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()        
    context['form']= form
    return render(request, "crudApp/create_view.html", context)
    #Retrive view
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Student.objects.all()   
    return render(request, "crudApp/list_view.html", context)
    # pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["data"] = Student.objects.get(id = id)    
    return render(request, "crudApp/detail_view.html", context)
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Student, id = id)
    # pass the object as instance in form
    form = StudentForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/student")
    # add form dictionary to context
    context["form"] = form
    return render(request, "crudApp/update_view.html", context)
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Student, id = id)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/student")
    return render(request, "crudApp/delete_view.html", context)
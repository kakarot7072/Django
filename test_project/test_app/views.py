from django.shortcuts import render, redirect
from .forms import tableform
# Create your views here.
from .models import table


def home(request):
    projects = table.objects.all()
    context = {'work': projects}
    return render(request, "template1.html", context)

def user(request, cookie):
    projectobj = table.objects.get(id = cookie)
    tags = projectobj.tags.all()
    return render(request, "template2.html", {"project": projectobj, 'tags':tags})

def createproject(request):
    form = tableform()

    if request.method == 'POST':
        form = tableform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('first')

    context = {'page': form}
    return render(request, "form.html", context)

def updateproject(request, pk):
    projectobj = table.objects.get(id=pk)
    form = tableform(instance=projectobj)

    if request.method == 'POST':
        form = tableform(request.POST, request.FILES, instance=projectobj)
        if form.is_valid():
            form.save()
            return redirect('first')
    context = {'page': form}
    return render(request, "form.html", context)

def deleteproject(request, pk):
    project = table.objects.get(id=pk)
    form = tableform(instance=project)

    if request.method == 'POST':
        project.delete()
        return redirect('first')
    context = {'object':project}
    return render(request, "delete.html", context)

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

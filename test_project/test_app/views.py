from django.shortcuts import render, redirect
from .forms import tableform
# Create your views here.
from .models import table
from django.http import HttpResponse

projectlist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'Description': 'A full func. Website'
    },
    {
        'id': '2',
        'title': 'Social Website',
        'Description': 'A full func. Website'
    },
    {
        'id': '3',
        'title': 'Food Website',
        'Description': 'Food Lowers Website'
    }
]

def home(request):
    msg = "I am Data."
    number = 10
    context = {
        'message': msg,
        'num': number,
        'work': projectlist,
    }

    projects = table.objects.all()
    context = {"work": projects}
    return render(request, "template1.html", context)

def user(request, cookie):
    projectobj = None
    for a in projectlist:
        if a["id"] == cookie:
            projectobj = a
    return render(request, "template2.html", {"project": projectobj})

def createproject(request):
    form = tableform()

    if request.method == 'POST':
        form = tableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('first')

    context = {'page': form}
    return render(request, "form.html", context)
from django.shortcuts import render, redirect
from .models import Profile
from .form import tableform

# Create your views here.

def user_profile(request):
    return render(request, 'profile.html')

def createprofile(request):
    form = tableform()

    if request.method == 'POST':
        form = tableform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    context = {'profile_page': form}
    return render(request, "profile_form.html", context)
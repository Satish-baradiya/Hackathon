from django.shortcuts import render, redirect
from django.http import HttpResponse
from Portal.forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = RegistrationForm()
    
    return render(request, "register.html",{
        "form":form
    }) 


def home(requsest):
    return HttpResponse("Welcome")

def login(request):
    return render(request, "login.html")
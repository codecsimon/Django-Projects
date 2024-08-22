from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# from .forms import RegisterForm
from .forms import UserForm
from .models import Users
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import login,logout


def index(request):
    return render(request,'index.html')

def logging(request):
    fort=Users.objects.all().values()
    context={'users':fort,}
    return render(request,'logged_in.html',context)

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        usert=Users.objects.all()
        if usert.filter(name=name).exists():
            fort=usert.filter(name=name)
            return redirect('logging')
        else:
            return HttpResponse("User does not exist")
    return render(request,'login.html')
def seal(request):
    form=UserForm()
    if request.method == 'POST':
        user=UserForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponse("Registration Successful")
        
    
    return render(request,'seal.html',{'form':form})
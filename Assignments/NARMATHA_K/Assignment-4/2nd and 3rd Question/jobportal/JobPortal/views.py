from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        candidates=Candidates.objects.filter(company__name=request.user.username)
        context={
            'candidates':candidates,
        }
        return render(request,'hr.html',context)
    else:
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'Jobseeker.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
       return render(request,'login.html')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=UserCreationForm()
        if request.method=='POST':
            Form=UserCreationForm(request.POST)
            if Form.is_valid():
                currUser=Form.save()
                Company.objects.create(user=currUser,name=currUser.username)
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)

def applyPage(request):
    form=ApplyForm()
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'apply.html',context)
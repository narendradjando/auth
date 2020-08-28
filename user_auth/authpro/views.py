from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authpro import forms
from django.http import *
#from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'test/home.html')

@login_required
def javaexams(request):
    return render(request,"test/javaexams.html")

@login_required
def bankexams(request):
    return render(request,"test/bankexams.html")

@login_required
def campusexams(request):
    return render(request,"test/campusexams.html")

def logout(request):
    return render(request,'test/logout.html')


def signup(request):
    form=forms.signupform()
    if request.method=='POST':
        form=forms.signupform(request.POST)
        User=form.save()
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,"test/signup.html",{"form":form})

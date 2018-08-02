
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import View
import json
def Homeview(request):
    if not request.user.is_authenticated():
         return render(request,'social_sites/login.html')
    else:
        return render(request,'social_sites/home.html',{'user':request.user.username})

    
class LoginCheckFormView(View):
    def get(self,request):
        username=request.GET.get('name',None)
        password=request.GET.get('pass',None)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            k=True
        else:
            k=False
        data={
            'is_valid':k,
        }
        return JsonResponse(data)

def logout_view(request):
    logout(request)
    return redirect('social_site:home')

class Sign_Up(View):
    def get(self,request):
        return render(request,'social_sites/register.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username,email=email,password=password)
        profile=Profile.objects.get(user=user)
        profile.mail=email
        profile.save()
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('social_site:home')

def check(request):
    username=request.GET.get('name',None)
    mail=request.GET.get('mail',None)
    data = {
        'name_is_taken': User.objects.filter(username__iexact=username).exists(),
        'mail_is_taken': User.objects.filter(email=mail).exists(),
    }
    return JsonResponse(data)

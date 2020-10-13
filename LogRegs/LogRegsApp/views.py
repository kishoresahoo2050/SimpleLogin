from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages
# Create your views here.

def index(req):
     if req.method  == 'POST':
          email     = req.POST['email']
          password  = req.POST['password']
          cursor = User.objects.filter(email=email,password=password)
          # return HttpResponse(cursor)
          if cursor:
                    print(cursor)
                    return render(req,'dashboard.htm',{'name':cursor}) 
          else:
               messages.info(req,"Invalid Email/Password")
               return redirect('login') 
     else:
          return render(req,'index.htm')

def register(req):
     if req.method == 'POST':
          user  = User()
          user.name       = req.POST['uname']
          user.email      = req.POST['email']
          user.num        = req.POST['num']
          user.password   = req.POST['password']
          if user.name=='' or user.email=='' or user.num=='' or user.password == '':
               messages.info(req,"Some Fields Are Missing,Please Checked")
               return redirect('register')
          else:
               user.save()
               return redirect('login')
          
     
     else:
           return render(req,'register.htm')
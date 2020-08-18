from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth  import  authenticate,login as dj_login,logout
from django.contrib.auth.models  import User,auth
from django.contrib.auth.forms import UserCreationForm
from assignment.models import Detailsofuser

# Create your views here.

def index(request):
    return render(request,'assignment/index.html')  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            dj_login(request, user)

            #login(request, user)
            return render(request,"assignment/index.html",{})
        else:
            return render(request,"assignment/signup.html")
    else:
        return render(request,"assignment/login.html")
        
def signup(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                
                user = User.objects.create_user(username=username,password=password,email=email)
                user.password = password
                user.set_password(user.password)
                user.is_staff=False
                user.is_superuser=False
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,'assignment/signup.html')


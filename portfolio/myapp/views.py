from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Home(request):
    return render(request, "index.html")

def Skill(request):
    return render(request, "skill.html")

def Projects(request):
    return render(request, "projects.html")

def HandleSignup(request):
    if request.method=="POST":
        # print("i am post request")
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        user_password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if user_password!=confirm_password:
            return HttpResponse("password not matching")
        
        if len(user_password)<5:
            return HttpResponse("password must be greater then 5")

        myuser=User.objects.create_user(email,email,user_password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        return redirect('/login')
        # print(first_name,last_name,email,user_password,confirm_password)

    # print("i am a function request")
    return render(request, "signup.html")

def HandleLogin(request):
    return render(request, "login.html")
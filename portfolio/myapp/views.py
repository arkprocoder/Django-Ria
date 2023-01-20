from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myapp.models import Contact
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
            messages.warning(request, "Password Incorrect")
            return redirect('/signup')
        
        if len(user_password)<5:
            messages.warning(request, "Password Must be Greater then 4 chars")
            return redirect('/signup')

        try:
            if User.objects.get(username=email):
                messages.error(request, "Email is already taken")
                return redirect('/signup')

        except:
            pass    
        try:
            if User.objects.get(email=email):
                messages.error(request, "Email is already taken")
                return redirect('/signup')

        except:
            pass    

        myuser=User.objects.create_user(email,email,user_password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request, "Signup Success Please Login")
        return redirect('/login')
        # print(first_name,last_name,email,user_password,confirm_password)

    # print("i am a function request")
    return render(request, "signup.html")

def HandleLogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        user_password=request.POST.get('pass1') 
        # print(email,user_password)
        myuser=authenticate(username=email,password=user_password)
        if myuser is not None:
            login(request, myuser)
            messages.info(request, f"Login Success Welcome")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/login")

    return render(request, "login.html")


def handleLogout(request):
    logout(request)
    messages.success(request, "logout Success")
    return redirect("/login")



def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('num')
        obj=Contact(name=name,email=email,description=desc,phone=phone)
        obj.save()
        messages.success(request, f"Thanks for contacting us {name}. We will get back you soon")
        return redirect("/contact")
    return render(request, "contact.html")
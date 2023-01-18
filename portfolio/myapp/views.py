from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "index.html")

def Skill(request):
    return render(request, "skill.html")

def Projects(request):
    return render(request, "projects.html")
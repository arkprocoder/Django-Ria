from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('skill',views.Skill,name="skill"),
    path('projects',views.Projects,name="Projects")
]

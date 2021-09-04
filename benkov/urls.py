"""benkov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path , include
from admin.models import contest, News

def asosiy(request):
    return render(request, 'asosiy.html')
    
def konkurs(request):
    data={
        'Contes': contest.objects.all().order_by('-id')
    }
    return render(request, 'konkurs.html', data)
def news(request):
    data={
        'News': News.objects.all().order_by('-id')
    }
    return render(request, 'news.html', data)
def courses(request):
    return render(request, 'courses.html')
def contact(request):
    return render(request,'contact.html')
def admin(request):
    return render(request,'admin.html')
urlpatterns = [
    path('',asosiy),
    path('admin/', include('admin.urls')),
    path('contest/', konkurs),
    path('news/', news),
    path('courses/',courses),
    path('contact/',contact),
    path('raxbarlar/',admin)
]

from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import contest, News
from django.core.files.storage import FileSystemStorage

def admin(request):
    return render(request,'homeAdmin.html')
def newsList(request):
    data= {
        'News': News.objects.all().order_by('-id')
    }
    return render(request,'newsList.html',data)
def newAdd(request):
    if request.method == 'POST':
        kns = News()
        kns.name = request.POST['name']


        fs = FileSystemStorage()
        image =  request.FILES['imageUrl']

        fs.save(image.name, image)

        kns.imageUrl = fs.url(image)

        
        kns.description =request.POST['description']
        kns.info =request.POST['info']
        kns.save()
        return redirect('/admin/')
    return render(request, 'newAdd.html')


def contestList(request):
    data = {
        'Contes': contest.objects.all().order_by('-id')
    }
    return render(request, 'konkursList.html', data)

def contestAdd(request):
    if request.method == 'POST':
        kns = contest()
        kns.name = request.POST['name']


        fs = FileSystemStorage()
        image =  request.FILES['imageUrl']

        fs.save(image.name, image)

        kns.imageUrl = fs.url(image)

        
        kns.description =request.POST['description']
        kns.prize =request.POST['prize']
        kns.info =request.POST['info']
        kns.save()
        return redirect('/admin/')
    return render(request, 'contestAdd.html')

def deleteContest(request,userid):
    kns = contest.objects.get(id=userid)
        
    kns.delete()
    return redirect('/admin/contest/')
def deleteNews(request,userid):
    new = News.objects.get(id=userid)
    new.delete()
    return redirect('/admin/newsList/')

from django.shortcuts import render
from django.urls import path , include
from .views import *
from .models import contest, News
from django.conf.urls.static import static
from django.conf import settings
from django.core.files.storage import FileSystemStorage

urlpatterns = [
    path('', admin),
    path('contest/', contestList),
    path('contest/delete/<int:userid>', deleteContest),
    path('contestAdd/', contestAdd),
    path('newAdd/', newAdd),
    path('newsList/', newsList),
    path('newsList/delete/<int:userid>', deleteNews),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

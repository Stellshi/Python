from django import http
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound,Http404
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse('Страница приложения women.')\
        
def categories(request, catid):
    return HttpResponse(f'<h1>Статья по категориям</h1><p>{catid}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def archive(requedt,year):
    if int(year) > 2020:
        raise Http404()



def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')



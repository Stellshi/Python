from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse('Страница приложения women.')\
        
def categories(request, catid):
    return HttpResponse(f'<h1>Статья по категориям</h1><p>{catid}</p>')



def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')



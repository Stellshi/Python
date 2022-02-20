from unicodedata import name
from django.urls import path, re_path

from .views import *

urlpatterns = [
    
    path('', index, name='home'),
    path('cats/<int:catid>/',categories),
    
]

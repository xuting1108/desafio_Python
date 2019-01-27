from django.shortcuts import render

# Create your views here.
#Esta é a view mais simples possível no Django. Para chamar a view, nós temos que mapear a URL - e por isto nós precisamos da URLconf;
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
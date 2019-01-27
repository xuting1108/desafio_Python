
#Para criar uma URLconf no diretório polls, Crie uma aquivo chamado urls.py. Agora seu diretório da aplicação deve ficar como:
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
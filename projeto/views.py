from django.http import HttpResponse
from django.shortcuts import render

def visualizar_home(request):
    return render(request, 'home.html')

def visualizar_login(request):
    return render(request,'users/login.html')
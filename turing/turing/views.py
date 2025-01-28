# from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def homepage(request):
    # return HttpResponse('O Jogo da Imitação')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("My About Page.")
    return render(request, 'about.html')

def story1(request):
    return render(request, 'story1.html')

def story2(request):
    return render(request, 'story2.html')

def story3(request):
    return render(request, 'story3.html')

def story4(request):
    return render(request, 'story4.html')

def choose(request):
    return render(request, 'choose.html')

def chat(request):
    return render(request, 'chat.html')


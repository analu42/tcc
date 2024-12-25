# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('O Jogo da Imitação')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("My About Page.")
    return render(request, 'about.html')
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(req: HttpRequest) -> HttpResponse:
    return render(req, 'main/inicial.html')

def help(req: HttpRequest) -> HttpResponse:
    return render(req, 'main/help.html')
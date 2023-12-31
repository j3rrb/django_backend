from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
from datetime import datetime

from .models import Access, Page, Topic
from .forms import CreateCarForm, CreatePetForm


def index_view(req: HttpRequest) -> HttpResponse:
    template = loader.get_template("main/inicial.html")

    return HttpResponse(
        template.render({"data": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}, req)
    )


def topic_view(req: HttpRequest) -> HttpResponse:
    data = Topic.objects.all()
    data_to_render = {"title": "Tópicos", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))


def page_view(req: HttpRequest) -> HttpResponse:
    data = Page.objects.all()
    data_to_render = {"title": "Página", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))


def accesses_view(req: HttpRequest) -> HttpResponse:
    data = Access.objects.all()
    data_to_render = {"title": "Acessos", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))


def create_car(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        form = CreateCarForm(req.POST)

        if form.is_valid():
            return render(req, "main/obrigado.html", {"data": form.cleaned_data})
    else:
        form = CreateCarForm()

    return render(req, "main/create-car.html", {"form": form})


def create_pet(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        form = CreatePetForm(req.POST)

        if form.is_valid():
            form.save()
            return render(req, "main/obrigado.html", {"data": form.cleaned_data})
    else:
        form = CreatePetForm()

    return render(req, "main/create-pet.html", {"form": form})


def thank_you(req: HttpRequest) -> HttpResponse:
    return render(req, "main/obrigado.html")


def calculator(req: HttpRequest) -> HttpResponse:
    return render(req, "main/calculadora.html")

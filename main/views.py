from django.http import HttpResponse
from django.template import loader

from .models import Access, Page, Topic


def topic_view(req):
    data = Topic.objects.all()
    data_to_render = {"title": "Tópicos", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))


def page_view(req):
    data = Page.objects.all()
    data_to_render = {"title": "Página", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))


def accesses_view(req):
    data = Access.objects.all()
    data_to_render = {"title": "Acessos", "data": data}
    template = loader.get_template("main/index.html")

    return HttpResponse(template.render(data_to_render, req))

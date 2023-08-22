from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("topicos/", views.topic_view, name="topicos"),
    path("acessos/", views.accesses_view, name="acessos"),
    path("paginas/", views.page_view, name="paginas"),
]
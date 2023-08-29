from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.topic_view),
    path("topicos", views.topic_view, name="topicos"),
    path("acessos", views.accesses_view, name="acessos"),
    path("paginas", views.page_view, name="paginas"),
    path("criar-carro", views.create_car, name="criar-carro"),
    path('criar-pet', views.create_pet, name='criar-pet'),
    path("obrigado", views.thank_you, name="obrigado"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    path('post/new/', views.adicionar_postagem, name="adicionar_postagem"),
    path('edit_postagem/<int:pk>/', views.edit_postagem, name="edicao_postagem")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('ajustar/<int:produto_id>/', views.ajustar_estoque, name='ajustar_estoque'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('historico/', views.historico_estoque, name='historico_estoque'),
]

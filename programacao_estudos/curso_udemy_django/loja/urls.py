from django.urls import path
from loja.views import mensagem_produto

urlpatterns = [
    path('produtos/', mensagem_produto),
]

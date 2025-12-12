from django.shortcuts import render

# Create your views here.
def mensagem_inicial(request):
    return render(request, 'loja/home.html')

def mensagem_produto(request):
    return render(request, 'loja/produto.html')

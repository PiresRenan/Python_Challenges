from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, MovimentoEstoque


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})


def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        produto = Produto(nome=nome, quantidade=quantidade)
        produto.save()
        movimento_entrada = MovimentoEstoque(
            produto=produto,
            quantidade=quantidade,
            tipo_movimento='E'
        )
        movimento_entrada.save()
        return redirect('lista_produtos')
    return render(request, 'estoque/adicionar_produto.html')


def ajustar_estoque(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        tipo_movimento = request.POST.get('tipo_movimento')
        if tipo_movimento == 'E':
            produto.quantidade += int(quantidade)
        else:
            produto.quantidade -= int(quantidade)
        produto.save()
        movimento = MovimentoEstoque(produto=produto, quantidade=quantidade, tipo_movimento=tipo_movimento)
        movimento.save()
        return redirect('lista_produtos')
    return render(request, 'estoque/ajustar_estoque.html', {'produto': produto})


def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    movimentos = MovimentoEstoque.objects.filter(produto=produto)
    movimentos.delete()
    produto.delete()
    return redirect('lista_produtos')


def historico_estoque(request):
    movimentos = MovimentoEstoque.objects.all()
    return render(request, 'estoque/historico_estoque.html', {'movimentos': movimentos})

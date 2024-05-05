from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class MovimentoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tipo_movimento = models.CharField(max_length=1, choices=[('E', 'Entrada'), ('S', 'Saída')])
    data_movimento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto} - {self.tipo_movimento}"

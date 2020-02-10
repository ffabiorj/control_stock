from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from product.models import Product

MOVIMENT = (
    ('e', 'entrada'),
    ('s', 'saída'),
)

class Stock(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENT)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pk} - {self.nf} - {self.created.strftime("%d/%m/%Y")}'

    def nf_format(self):
        return str(self.nf).zfill(3)


class StockItems(models.Model):
    estoque = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk} - {self.estoque.pk} - {self.produto}'

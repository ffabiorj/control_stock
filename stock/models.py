from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from product.models import Product

MOVIMENT = (
    ('e', 'entry'),
    ('s', 'left'),
)

class Stock(TimeStampedModel):
    employ = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice = models.PositiveIntegerField('invoice', null=True, blank=True)
    moviment = models.CharField(max_length=1, choices=MOVIMENT)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk)


class StockItems(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk} - {self.stock.pk} - {self.product}'

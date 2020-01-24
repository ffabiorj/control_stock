from django.db import models

class Product(models.Model):
    importad = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    product = models.CharField(max_length=100, unique=True)
    price = models.DecimalField('price', max_digits=7, decimal_places=2)
    stock = models.IntegerField('current stock')
    minimum_stock = models.PositiveIntegerField('minimum stock')

    class Meta:
        ordering = ('product',)

    def __str__(self):
        return self.product

    
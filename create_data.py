import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "control_stock.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from product.models import Product


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProductClass:

    @staticmethod
    def create_products(products):
        Product.objects.all().delete()
        aux = []
        for product in products:
            data = dict(
                product=product,
                importad=choice((True, False)),
                ncm=Utils.gen_digits(8),
                price=random() * randint(10, 50),
                stock=randint(10, 200),
            )
            obj = Product(**data)
            aux.append(obj)
        Product.objects.bulk_create(aux)


produtos = (
    'Apontador',
    'Caderno 100 folhas',
    'Caderno capa dura 200 folhas',
    'Caneta esferográfica azul',
    'Caneta esferográfica preta',
    'Caneta esferográfica vermelha',
    'Durex',
    'Giz de cera 12 cores',
    'Lapiseira 0.3 mm',
    'Lapiseira 0.5 mm',
    'Lapiseira 0.7 mm',
    'Lápis de cor 24 cores',
    'Lápis',
    'Papel sulfite A4 pacote 100 folhas',
    'Pasta elástica',
    'Tesoura',
)

tic = timeit.default_timer()

ProductClass.create_products(produtos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)
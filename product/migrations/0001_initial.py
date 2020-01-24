# Generated by Django 3.0.2 on 2020-01-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importad', models.BooleanField(default=False)),
                ('ncm', models.CharField(max_length=8, verbose_name='NCM')),
                ('product', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='price')),
                ('stock', models.IntegerField(verbose_name='current stock')),
                ('minimum_stock', models.PositiveIntegerField(verbose_name='minimum stock')),
            ],
            options={
                'ordering': ('product',),
            },
        ),
    ]

# Generated by Django 3.1.3 on 2022-06-22 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]

# Generated by Django 4.1 on 2022-09-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

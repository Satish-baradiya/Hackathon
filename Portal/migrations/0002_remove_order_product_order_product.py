# Generated by Django 4.1 on 2022-09-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='Portal.product'),
        ),
    ]

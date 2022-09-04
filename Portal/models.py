from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price  = models.FloatField(default=0)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0)
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product = models.ManyToManyField(Product)
    ordered_quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

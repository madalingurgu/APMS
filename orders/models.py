from django.db import models

# Create your models here.

class Order(models.Model):
    order_number = models.IntegerField()
    customer = models.CharField(max_length=255)
    drawing_number = models.CharField(max_length=50)
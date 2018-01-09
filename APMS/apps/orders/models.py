from django.db import models

# Create your models here.

class Order(models.Model):
    order_number = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=255)
    drawing_number = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    

            

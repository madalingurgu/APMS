from django.db import models

# Create your models here.

class Entry(models.Model):

    order_type = models.CharField(max_length=50)
     
        
    def __str__(self):
        return self.order_type
    
    

class Order(models.Model):
    order_number = models.IntegerField(unique=True)
    drawing_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    
    slug = models.SlugField(unique=True)
    post_date = models.DateTimeField('date posted')
    
    entry = models.ForeignKey(Entry, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.slug

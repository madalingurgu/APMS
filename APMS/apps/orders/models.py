from django.db import models

# Create your models here.




class Order(models.Model):
    order_number = models.IntegerField(unique=True)
    drawing_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    post_date = models.DateTimeField('date posted')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
        
class Sample(models.Model):
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description
    
    
FAVE_CHOICES = ( 
    ('A','Order'),
    ('C','Sample'),
)
    
        
class Request(models.Model):

    type_of_fave = models.CharField( max_length=1, 
        choices=FAVE_CHOICES, null=True, on_delete=models.SET_NULL)
#    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
#    sample = models.ForeignKey(Sample, null=True, on_delete=models.SET_NULL)
    order_by = models.CharField(max_length=50, null=True)

#    def __str__(self):
#        return self.order
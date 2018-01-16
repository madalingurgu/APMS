from django.db import models

# Create your models here.


        
class Sample(models.Model):
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description


TYPE_CHOICES = ( 
    ('ORDER','Order'),
    ('SAMPLE','Sample'),
)

TYPE_STATUS = ( 
    ('QUEUE','Queue'),
    ('WIP','Wip'),
    ('COMPLETE','Complete'),
    ('HOLD','Hold'),
)
class Request(models.Model):
    
    type_of_choice = models.CharField( max_length=20,
        choices=TYPE_CHOICES, default='ORDER')
    order_by = models.CharField(max_length=50, null=True)
    post_date = models.DateTimeField('date posted')
    requested_date = models.DateTimeField('request date')
    status = models.CharField( max_length=20,
        choices=TYPE_STATUS, default='QUEUE')
    
    def __str__(self):
        return self.status
        

class Order(models.Model):
    order_number = models.AutoField(primary_key =True)
    drawing_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    request_type = models.ForeignKey(Request, null=True, blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.slug
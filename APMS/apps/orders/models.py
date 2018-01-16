from django.db import models

# Create your models here.


TYPE_CHOICES = ( 
    ('ORDER','Order'),
    ('SAMPLE','Sample'),
    ('ECR','Ecr'),
    ('ERF','Erf'),
)

TYPE_STATUS = ( 
    ('QUEUE','Queue'),
    ('WIP','Wip'),
    ('COMPLETE','Complete'),
    ('HOLD','Hold'),
)
class Request(models.Model):
    project_no = models.IntegerField(primary_key=True)
    r_type = models.CharField( max_length=20,
        choices=TYPE_CHOICES, default='ORDER')
    description = models.CharField(max_length=255, null=True)
    customer = models.CharField(max_length=50, null=True)
    order_by = models.CharField(max_length=50, null=True)
    post_date = models.DateTimeField('date posted')
    estimate = models.DateField('request date')
    status = models.CharField( max_length=20,
        choices=TYPE_STATUS, default='QUEUE')
    
    def __int__(self):
        return self.project_no
        

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    delivery = models.DateField('delivery date')
    request_r = models.ForeignKey(Request, null=True, blank=True,
        on_delete=models.SET_NULL)

    def __int__(self):
        return self.order_id
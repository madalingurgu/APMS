from django.db import models

# Create your models here.

################################################################################        
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)
    user = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

################################################################################
TYPE_PRODUCT = ( 
    ('BBT','BBT'),
    ('BTY','BTY'),
    ('BLS','BLS'),
    ('BRS','BRS'),
    ('CKS','CKS'),
    ('FMI','FMI'),
    ('GRD','GRD'),
    ('LID','LID'),
    ('MFT','MFT'),
    ('SHR','SHR'),
    ('SPN','SPN'),
    ('TRL','TRL'),
)
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    p_type = models.CharField( max_length=20,
        choices=TYPE_PRODUCT, default='BBT')
    drawing_no = models.IntegerField()
    description = models.CharField(max_length=255)
    engineer = models.ForeignKey(Staff, null=True, blank=True,
        on_delete=models.SET_NULL)
    technology = models.CharField(max_length=500)


    def __int__(self):
        return self.drawing_no

################################################################################        
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    adress = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=100)
    sales_responsable = models.ForeignKey(Staff, null=True, blank=True,
        on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.name
        
################################################################################
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    delivery = models.DateField('delivery date')

    def __int__(self):
        return self.order_id
        
################################################################################        
class Engineering(models.Model):
    eng_id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=50, null=True)
    instructions = models.CharField(max_length=500, null=True)
    request_date = models.DateField('request date')
    
    def __int__(self):
        return self.eng_id

################################################################################
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
    product = models.ForeignKey(Product, null=True, blank=True,
        on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True,
        on_delete=models.SET_NULL)
    order_by = models.ForeignKey(Staff, null=True, blank=True,
        on_delete=models.SET_NULL)
    #
    post_date = models.DateTimeField('date posted')
    estimate = models.DateField('estimate date')
    status = models.CharField( max_length=20,
        choices=TYPE_STATUS, default='QUEUE')
    order = models.ForeignKey(Order, null=True, blank=True,
        on_delete=models.SET_NULL)
    eng = models.ForeignKey(Engineering, null=True, blank=True,
        on_delete=models.SET_NULL)
    
    def __int__(self):
        return self.project_no
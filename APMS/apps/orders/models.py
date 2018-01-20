from django.db import models

# Create your models here.

################################################################################        
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)

    
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
    technology = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return str(self.p_type)+' '+str(self.drawing_no)

################################################################################        
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    sales_responsable = models.ForeignKey(Staff, null=True, blank=True,
        on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.name
        
################################################################################
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)


    def __str__(self):
        return 'Order'+'-'+str(self.order_id)
        
################################################################################        
class Engineering(models.Model):
    eng_id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=50, null=True, blank=True)
    instructions = models.CharField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return 'Engineering'+'-'+str(self.eng_id)

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
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField('date posted')
    order = models.ForeignKey(Order, null=True, blank=True,
        on_delete=models.SET_NULL)
    eng = models.ForeignKey(Engineering, null=True, blank=True,
        on_delete=models.SET_NULL)
    responsable = models.ForeignKey(Staff, null=True, blank=True,
        on_delete=models.SET_NULL)    
    request_date = models.DateField('request date', null=True, blank=True)    
    estimate = models.DateField('estimate completion date', null=True, blank=True)
    status = models.CharField( max_length=20,
        choices=TYPE_STATUS, default='QUEUE')
    comments = models.CharField(max_length=255, null=True, blank=True)
    
    
    def __int__(self):
        return self.project_no
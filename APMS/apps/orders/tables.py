import django_tables2 as tables
from orders.models import Staff

class StaffTable(tables.Table):
    class Meta:
        model = Staff
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-light'}
#        attrs={'th': {'class': 'row'}}
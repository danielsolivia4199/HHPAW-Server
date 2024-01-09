from django.db import models
from .employee import Employee

class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    is_closed = models.BooleanField()

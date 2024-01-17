from django.db import models
from .order import Order

class Revenue(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_amount = models.DecimalField(max_digits=5, decimal_places=2)
    tip_amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    

from django.db import models
from .order import Order

class Revenue(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_amount = models.IntegerField()
    tip_amount = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False)
    

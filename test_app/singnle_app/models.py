from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField() 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item_quantity = models.ForeignKey('ItemQuantity', on_delete=models.CASCADE,blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    

class ItemQuantity(models.Model):   
    quantity = models.IntegerField(default=1, null=True)
    
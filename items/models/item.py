from django.db import models
from django.db.models.deletion import CASCADE

from items.models.Item_unit import Unit
from .category import Category


class Item(models.Model):
    sku = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_quantity= models.IntegerField()
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)


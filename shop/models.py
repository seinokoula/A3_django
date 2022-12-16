from django.db import models


# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_stock = models.IntegerField()
    item_image = models.TextField()

    def __str__(self):
        return self.item_name


class ItemsModel:
    pass
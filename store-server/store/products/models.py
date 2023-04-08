from django.db import models
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
# import django
# django.setup()

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
     name = models.CharField(max_length=256)
     description = models.TextField(null=True, blank=True)
     size = models.CharField(max_length=256)
     price = models.DecimalField(max_digits=7, decimal_places=2)
     quantity = models.PositiveIntegerField(default=0)
     image = models.ImageField(upload_to='products_images')
     category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

     def __str__(self):
        return self.name + ', ' + self.description

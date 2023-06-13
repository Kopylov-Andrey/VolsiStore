from django.db import models

from users.models import User
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
# import django
# django.setup()

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категорию товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name

class Product(models.Model):
     name = models.CharField(max_length=256)
     description = models.TextField(null=True, blank=True)
     size = models.CharField(max_length=256)
     price = models.DecimalField(max_digits=7, decimal_places=2)
     quantity = models.PositiveIntegerField(default=0)
     image = models.ImageField(upload_to='products_images')
     category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

     class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

     def __str__(self):
        return self.name + ', ' + self.description

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.products.name}'

    def sum(self):
        return self.products.price * self.quantity











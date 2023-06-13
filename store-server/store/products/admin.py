from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product, Basket

# admin.site.register(Product)
admin.site.register(ProductCategory)
# admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'size', ('price', 'quantity'), 'image',  'category')
    search_fields = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('products', 'quantity')
    extra = 0

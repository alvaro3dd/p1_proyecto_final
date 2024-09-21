from django.contrib import admin
from .models import Product,Category,Brand

admin.site.register(Brand)
admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Product)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'stock_quantity', 'brand', 'price')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')



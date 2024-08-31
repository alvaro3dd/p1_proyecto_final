from django.db import models

class Category(models.Model):
    ''' Groups the products into categories like "Laptops", "Monitors", etc.'''
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

class Brand(models.Model):
    '''Represents the brand of the PC equipment'''
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    specs = models.JSONField(null=True, blank=True)  # To store specifications like RAM, Storage, etc.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'

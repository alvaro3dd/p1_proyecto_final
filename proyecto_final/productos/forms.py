from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Or specify the fields you want, e.g., ['name', 'price', 'category']

from django.urls import path, include
from . import views

app_name = 'productos'

urlpatterns = [
  path("", views.index, name ="index"),
  path("product/list", views.product_list, name = "product_list"),
  path('product/create', views.product_create, name='product_create'),

  
]

                      
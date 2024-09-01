
from django.urls import path, include
from . import views

app_name = 'productos'

urlpatterns = [
  path("", views.index, name ="index"),
  path("product/list", views.product_list, name = "product_list"),
  path('product/create', views.product_create, name='product_create'),
  path('product/detail/<int:pk>', views.product_detail, name ='product_detail' ),
  path('product/update/<int:pk>', views.product_update, name ='product_update' ),
  path('product/delete/<int:pk>', views.product_delete, name ='product_delete' ),
]

                      
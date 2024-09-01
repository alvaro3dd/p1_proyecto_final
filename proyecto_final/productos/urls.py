
from django.urls import path, include
from . import views

app_name = 'productos'

urlpatterns = [
  path("", views.index, name ="index"),

  ##OLD Paths Func views
  #path("product/list", views.product_list, name = "product_list"),
  #path('product/create', views.product_create, name='product_create'),
  #path('product/detail/<int:pk>', views.product_detail, name ='product_detail' ),
  #path('product/update/<int:pk>', views.product_update, name ='product_update' ),
  #path('product/delete/<int:pk>', views.product_delete, name ='product_delete' ),


  ##NEW Paths Class-Based View (CBV)
    path(
        'product/list',
        views.ProductList.as_view(),
        name='product_list',
    ),

     path(
        'product/create',
        views.ProductCreate.as_view(),
        name='product_create',
    ),

    path(
        'product/detail/<int:pk>',
        views.ProductDetail.as_view(),
        name='product_detail',
    ),

     path(
        'product/update/<int:pk>',
        views.ProductUpdate.as_view(),
        name='product_update',
    ),

    path(
        'product/delete/<int:pk>',
        views.ProductDelete.as_view(),
        name='product_delete',
    ),

  


]

                      
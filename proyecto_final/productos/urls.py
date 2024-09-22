
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


 # ******* PRODUCTS 
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


 # ******* Category
  
    path(
        'category/list',
        views.CategoryList.as_view(),
        name = 'category_list'
    ),

    path(
        'category/create',
        views.CategoryCreate.as_view(),
        name='category_create',
    ),

    path(
        'category/detail/<int:pk>',
        views.CategoryDetail.as_view(),
        name='category_detail',
    ),

     path(
        'category/update/<int:pk>',
        views.CategoryUpdate.as_view(),
        name='category_update',
    ),

    path(
        'category/delete/<int:pk>',
        views.CategoryDelete.as_view(),
        name='category_delete',
    ),

 # ******* Brand 
  
    path(
        'brand/list',
        views.BrandList.as_view(),
        name = 'brand_list'
    ),

    path(
        'brand/create',
        views.BrandCreate.as_view(),
        name='brand_create',
    ),

    path(
        'brand/detail/<int:pk>',
        views.BrandDetail.as_view(),
        name='brand_detail',
    ),

    path(
        'brand/update/<int:pk>',
        views.BrandUpdate.as_view(),
        name='brand_update',
    ),

    path(
        'brand/delete/<int:pk>',
        views.BrandDelete.as_view(),
        name='brand_delete',
    ),




]

                      
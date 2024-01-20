from django.urls import path
from .views import product_list, product_detail,ProductView
from .views import IndexView #added for  html temp

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('', IndexView.as_view(), name='index'), #added for  html temp
    path('product/', ProductView.as_view(), name='product.html'),

]
from django.urls import path
from .views import product_list, product_detail
from .views import IndexView

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('', IndexView.as_view(), name='index'),
]
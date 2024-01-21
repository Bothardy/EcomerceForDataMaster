from django.urls import path
from .views import product_list, product_detail,ProductView,productpage,profiluser
from .views import IndexView #added for  html temp

urlpatterns = [

    path('product/', productpage, name='product.html'),
    path('profile/', profiluser, name='profile.html'),

]
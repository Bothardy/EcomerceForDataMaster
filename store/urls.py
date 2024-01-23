from django.urls import path
from .views import productpage,profiluser

urlpatterns = [

    path('product/', productpage, name='product.html'),
    path('profile/', profiluser, name='profile.html'),

]

from django.urls import path
from .views import productpage,profiluser,auth

urlpatterns = [

    path('product/', productpage, name='product.html'),
    path('profile/', profiluser, name='profile.html'),
    path('auth/', auth, name='auth.html'),

]

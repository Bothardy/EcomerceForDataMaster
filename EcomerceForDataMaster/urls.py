# EcomerceForDataMaster/urls.py
from django.contrib import admin
from django.urls import path, include
from store.views import home  # Import the view for the home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home.html'),  # Add this line for the root path
    path('store/', include('store.urls')),  # Include your app's URLs


]

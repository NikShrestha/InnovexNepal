from django.contrib import admin
from django.urls import include, path
from innovexnepalwebsite import views as innovex_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('innovexnepalwebsite.urls')),  # Include URLs from the app
]

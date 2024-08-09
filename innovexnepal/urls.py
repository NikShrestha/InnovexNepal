from django.contrib import admin
from django.urls import include, path
from innovexnepalwebsite import views as innovex_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', innovex_views.index, name='index'),  # Root URL for the index view
    path('innovexnepalwebsite/', include('innovexnepalwebsite.urls')),
]

from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add the home view here
    path('api/users/', include('users.urls')),
    path('api/workouts/', include('workouts.urls')),
]

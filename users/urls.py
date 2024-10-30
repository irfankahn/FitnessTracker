from django.urls import path
from .views import RegisterView, CustomAuthToken, LogoutView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),  # Use the root path for registration
    path('login/', CustomAuthToken.as_view(), name='login'),  # Login endpoint
    path('logout/', LogoutView.as_view(), name='logout'),     # Logout endpoint
]

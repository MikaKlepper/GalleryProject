from django.urls import path
from . import views  # Import the views module
from .views import *
#get_routes, MyTokenObtainPairView 
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.get_routes),
    path('register/', views.register, name='register'),
    path('profile/', views.get_or_update_profile),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path
from .views import RegisterView, Loginview, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', RegisterView.as_view(), name='login'),
    path('profile/', RegisterView.as_view(), name='profile')
]
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('registreren/', UserRegisterView.as_view(), name='register'),
]
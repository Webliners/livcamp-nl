from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registreren/', UserRegisterView.as_view(), name='register'),
    path('profiel_aanpassen/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profiel/', ShowProfilePageView.as_view(), name='profilepage'),
    path('<int:pk>/edit_profielpagina/', EditProfilePageView.as_view(), name='edit_profielpagina'),
    path('profielpagina_aanmaken/', CreateProfilePageView.as_view(), name='create_profilepage'),
]
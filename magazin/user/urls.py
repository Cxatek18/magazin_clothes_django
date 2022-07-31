from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    SendMessageToTelegramm,
)

urlpatterns = [
    path(
        'register-user/', UserRegisterView.as_view(), name='register_user',
    ),
    path(
        'login-user/', UserLoginView.as_view(), name='login_user',
    ),
    path(
        'logout-user/', UserLogoutView.as_view(), name='logout_user',
    ),
    path(
        'personal-account-user/<int:pk>/',
        UserDetailView.as_view(), name='personal_account_user',
    ),
    path(
        'contact-with-me/',
        SendMessageToTelegramm.as_view(), name='contact_with_me',
    ),
]

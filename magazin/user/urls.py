from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path(
        'register_user/', UserRegisterView.as_view(), name='register_user',
    ),
    path(
        'login_user/', UserLoginView.as_view(), name='login_user',
    ),
    path(
        'logout_user/', UserLogoutView.as_view(), name='logout_user',
    ),
]

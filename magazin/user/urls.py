from django.urls import path

from .views import (
    UserRegister,
)

urlpatterns = [
    path(
        'register_user/', UserRegister.as_view(), name='register_user',
    ),
]

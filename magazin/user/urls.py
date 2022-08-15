from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    SendMessageToTelegramm,
    UserUpdateInfoView,
    ListCouponUserView,
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
    path(
        'update-user-info/<int:pk>/',
        UserUpdateInfoView.as_view(), name='update_user_info',
    ),
    path(
        'list-coupons-list/',
        ListCouponUserView.as_view(), name='list_coupons_list',
    ),
]

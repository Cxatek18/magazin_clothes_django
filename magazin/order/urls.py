from django.urls import path

from .views import (
    OrderAllProductCartView,
    OrderOneProductInCartView,
    ListOrderView,
    DeleteOrderView,
    UpdateOrderUserView,
    UpdateOrderAdminView,
)

urlpatterns = [
    path(
        'order-all-product-cart/',
        OrderAllProductCartView.as_view(),
        name='order_all_product_cart',
    ),
    path(
        'order-one-product-cart/<int:pk>/',
        OrderOneProductInCartView.as_view(),
        name='order_one_product_cart',
    ),
    path(
        'list-order-product/',
        ListOrderView.as_view(),
        name='list_order_product',
    ),
    path(
        'delete-order/<int:pk>/',
        DeleteOrderView.as_view(), name='delete_order',
    ),
    path(
        'order-update-user/<int:pk>/',
        UpdateOrderUserView.as_view(),
        name='order_update_user',
    ),
    path(
        'order-update-admin/<int:pk>/',
        UpdateOrderAdminView.as_view(),
        name='order_update_admin',
    ),
]

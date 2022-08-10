from django.urls import path

from .views import (
    OrderAllProductCart,
    OrderOneProductInCart,
)

urlpatterns = [
    path(
        'order-all-product-cart/',
        OrderAllProductCart.as_view(),
        name='order_all_product_cart',
    ),
    path(
        'order-one-product-cart/<int:pk>/',
        OrderOneProductInCart.as_view(),
        name='order_one_product_cart',
    ),
]

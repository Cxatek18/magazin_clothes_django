from django.urls import path

from .views import (
    OrderAllProductCart,
)

urlpatterns = [
    path(
        'order-all-product-cart/',
        OrderAllProductCart.as_view(),
        name='order_all_product_cart',
    ),
]

from django.urls import path

from .views import (
    AddProductInCart,
)

urlpatterns = [
    path(
        'cart/add-product-in-cart/<int:pk>/',
        AddProductInCart.as_view(),
        name='add_product_in_cart',
    ),
]

from django.urls import path

from .views import (
    AddProductInCart,
    ListProductInCart,
    DeleteProductFromCart,
)

urlpatterns = [
    path(
        'add-product-in-cart/<int:pk>/',
        AddProductInCart.as_view(),
        name='add_product_in_cart',
    ),
    path(
        'list-product-in-cart/',
        ListProductInCart.as_view(),
        name='list_product_in_cart',
    ),
    path(
        'delete-product-in-cart/<int:pk>/',
        DeleteProductFromCart.as_view(),
        name='delete_product_in_cart',
    ),
]

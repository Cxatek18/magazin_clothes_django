from django.urls import path

from .views import (
    AddProductInCartView,
    ListProductInCartView,
    DeleteProductFromCartView,
    ChangeQtyProductInCartView,
)

urlpatterns = [
    path(
        'add-product-in-cart/<int:pk>/',
        AddProductInCartView.as_view(),
        name='add_product_in_cart',
    ),
    path(
        'list-product-in-cart/',
        ListProductInCartView.as_view(),
        name='list_product_in_cart',
    ),
    path(
        'delete-product-in-cart/<int:pk>/',
        DeleteProductFromCartView.as_view(),
        name='delete_product_in_cart',
    ),
    path(
        'change-product-qty-in-cart/<int:pk>/',
        ChangeQtyProductInCartView.as_view(),
        name='change_product_qty_in_cart',
    ),
]

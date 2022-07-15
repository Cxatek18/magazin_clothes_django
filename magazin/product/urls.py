from django.urls import path
from .views import (
    HomeProductView,
    CategoriesView,
    ProductDetailView,
    ProductCreateView,
)

urlpatterns = [
    path('', HomeProductView.as_view(),  name='home',),
    path(
        'category/v1/<int:category_id>/',
        CategoriesView.as_view(), name='category',
    ),
    path(
        'product/v1/<slug:product_slug>/',
        ProductDetailView.as_view(), name='product_detail',
    ),
    path(
        'product/create-product/',
        ProductCreateView.as_view(), name='create_product',
    ),
]

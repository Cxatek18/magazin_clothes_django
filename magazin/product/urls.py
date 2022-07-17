from django.urls import path
from .views import (
    HomeProductView,
    ProductManagementView,
    CategoriesView,
    BrandsView,
    ProductDetailView,
    ProductCreateView,
    UpdateProductView,
)

urlpatterns = [
    path('', HomeProductView.as_view(),  name='home',),
    path(
        'product/management_product/', ProductManagementView.as_view(),
        name='management_product',
    ),
    path(
        'brand/v1/<int:brand_id>/',
        BrandsView.as_view(), name='brand',
    ),
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
    path(
        'product/update-product/<int:pk>/',
        UpdateProductView.as_view(), name='update_product',
    ),
]

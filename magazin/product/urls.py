from django.urls import path
from .views import (
    HomeProductView,
    ProductManagementView,
    CategoriesView,
    BrandsView,
    ProductDetailView,
    ProductCreateView,
    UpdateProductView,
    DeleteProductView,
    AddingProductPhoto,
    CreateBrand,
    ListProductImageView,
    UpdateProductImageView,
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
    path(
        'product/delete-product/<slug:product_slug>/',
        DeleteProductView.as_view(), name='delete_product',
    ),
    path(
        'product/add-photo-product/<slug:product_slug>/',
        AddingProductPhoto.as_view(), name='add_photo_product',
    ),
    path(
        'product/create-brand/',
        CreateBrand.as_view(), name='create_brand',
    ),
    path(
        'product/list-photo-product/<slug:product_slug>/',
        ListProductImageView.as_view(), name='list_photo_product',
    ),
    path(
        'product/update-photo-product/<int:pk>/',
        UpdateProductImageView.as_view(), name='update_photo_product',
    ),
]

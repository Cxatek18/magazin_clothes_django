from django.urls import path
from .views import (
    HomeProductView,
    CategoriesView,
    ProductDetailView,
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
]

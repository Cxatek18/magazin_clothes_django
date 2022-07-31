from django.contrib import admin

from .models import (
    Product,
    Category,
    ProductImage,
    ProductColor,
    ProductBrand,
    ProductSize,
    FavoriteUserProduct,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name', 'slug', 'category',
        'updated_at', 'created_at',
        'price_now', 'status', 'quantity', 'gender'
    )
    list_display_links = (
        'id', 'product_name',
        'slug',
    )
    search_fields = (
        'id', 'product_name',
        'slug', 'gender'
    )
    list_editable = (
        'status', 'quantity',
        'gender'
    )
    list_filter = (
        'status', 'category',
        'gender',
    )
    readonly_fields = ('created_at',
                       'updated_at',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category_name',
        'slug_category',
    )
    list_display_links = (
        'id', 'category_name',
        'slug_category',
    )
    search_fields = (
        'id', 'category_name',
    )


class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image',
    )
    list_display_links = (
        'id', 'image',
    )


class ProductColorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'color',
    )
    list_display_links = (
        'id', 'color',
    )


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name', 'slug_brand',
    )
    list_display_links = (
        'brand_name',
    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'size_value', 'size_category',
    )
    list_display_links = (
        'size_value',
    )


class FavoriteUserProductAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'user',
    )
    list_display_links = (
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(FavoriteUserProduct, FavoriteUserProductAdmin)

from django.contrib import admin
from .models import (
    Product,
    Category,
    ProductImage,
    ProductColor,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name', 'slug', 'category',
        'updated_at', 'created_at',
        'price_now', 'status', 'quantity'
    )
    list_display_links = (
        'id', 'product_name',
        'slug',
    )
    search_fields = (
        'id', 'product_name',
        'slug',
    )
    list_editable = ('status', 'quantity')
    list_filter = ('status', 'category')
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductColor, ProductColorAdmin)

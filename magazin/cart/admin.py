from django.contrib import admin

from .models import (
    Cart,
    CartProduct
)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_name', 'total_products', 'final_price_cart',
        'total_discount_price', 'total_not_discount_price',
        'for_anonymous_user', 'in_order'
    )
    list_display_links = (
        'id', 'user_name',
    )
    search_fields = (
        'id', 'user_name',
    )
    list_editable = (
        'total_products', 'final_price_cart',
        'total_discount_price', 'total_not_discount_price',
        'for_anonymous_user', 'in_order'
    )
    list_filter = (
        'in_order', 'for_anonymous_user',
    )
    save_on_top = True


class CartProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cart', 'product_name', 'count_product',
        'final_price', 'final_total_discount',
        'final_price_not_discount'
    )
    list_display_links = (
        'id', 'cart',
    )
    search_fields = (
        'id', 'cart',
        'product_name',
    )
    list_editable = (
        'count_product', 'final_price',
        'final_total_discount', 'final_price_not_discount',
    )
    save_on_top = True


admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct, CartProductAdmin)

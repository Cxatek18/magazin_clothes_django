from django.contrib import admin

from .models import (
    Order,
)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_name', 'phone_number', 'address',
        'status_order', 'buying_type',
        'total_products', 'final_price_order', 'created_at',
        'updated_at'
    )
    list_display_links = (
        'id', 'user_name',
    )
    search_fields = (
        'id', 'user_name',
        'phone_number',
    )
    list_editable = (
        'status_order',
        'buying_type', 'total_products',
        'final_price_order',
    )
    list_filter = (
        'buying_type', 'status_order',
    )
    save_on_top = True


admin.site.register(Order, OrderAdmin)

from django.contrib import admin

from .models import (
    Stock
)


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'stock_name', 'image_stock',
    )
    list_display_links = (
        'id', 'stock_name',
    )
    search_fields = (
        'id', 'stock_name',
    )


admin.site.register(Stock, StockAdmin)

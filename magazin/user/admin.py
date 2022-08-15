from django.contrib import admin
from .models import (
    User,
    Coupon,
)


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'is_active',
        'is_staff', 'is_moderator', 'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'username', 'email')
    search_fields = (
        'id', 'username', 'email', 'city',
    )
    list_editable = (
        'is_active', 'is_staff', 'is_moderator',
    )
    list_filter = (
        'is_active', 'is_staff', 'is_moderator',
    )
    fields = (
        'username', 'email', 'is_active',
        'is_staff', 'is_moderator', 'password', 'ip_address',
        'city', 'сoupons_user'
    )


class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code_сoupon', 'valid_from',
        'valid_to', 'discount_сoupon',
        'active'
    )
    list_display_links = ('id', 'code_сoupon')
    search_fields = (
        'id', 'code_сoupon',
    )
    list_editable = (
        'active', 'discount_сoupon'
    )
    list_filter = (
        'active',
    )


admin.site.register(User, UsersAdmin)
admin.site.register(Coupon, CouponAdmin)

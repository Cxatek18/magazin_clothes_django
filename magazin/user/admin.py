from django.contrib import admin
from .models import (
    User,
)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active',
                    'is_staff', 'created_at',
                    'updated_at',)
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_editable = (
        'is_active', 'is_staff',
    )
    list_filter = (
        'is_active', 'is_staff',
    )
    fields = (
        'username', 'email', 'is_active',
        'is_staff', 'is_moderator', 'password', 'ip_address',
        'city',
    )


admin.site.register(User, UsersAdmin)

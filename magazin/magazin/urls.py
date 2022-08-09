from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = "product.views.handling_error_404"
handler403 = "product.views.handling_error_403"
handler400 = "product.views.handling_error_400"

urlpatterns = [
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

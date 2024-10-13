from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_service/', include('auth_service.urls')),
    path('', include('app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('product/', include('product.urls')),
    path('supplier/', include('supplier.urls')),
    path('shop/', include('shop.urls')),
    path('order/', include('order.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),

    path('inbox/', include('conversation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#never do that on production
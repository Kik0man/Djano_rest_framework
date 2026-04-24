from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('lms.urls')),      # эндпоинты курсов и уроков
    path('api/', include('users.urls')),    # эндпоинты профиля пользователя
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
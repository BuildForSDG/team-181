from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth-path/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path,incule,re_path
from django.conf import settings
from django.conf.urls.static import static

# Document
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schame_view(
    openapi.Info(
        title = "Snippets API",
        default_version = 'v1',
        description = "Test description",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email = "contact@snippets.local"),
        license = openapi.License(name = "BSD License"),
        ),
        public = True,
        permission_classes = (permissions.AllowAny,) ,
        )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',incude('universal.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/',schame_view.with_ui('swagger',cache_timeout = 0),name = "schame-swagger-ui"),
    path('redoc/',schame_view.with_ui('redoc',cache_timeout = 0),name = 'schame_redoc')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings)
    
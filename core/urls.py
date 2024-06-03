from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings
from core.settings import is_running_tests


schema_view = get_schema_view(
    openapi.Info(
        title="HydroponicsSystem",
        default_version="v1",
        description="Hydroponics System API documentation",
        contact=openapi.Contact(email="samekmat@gmail.com"),
        license=openapi.License(name="MIT License", url="https://opensource.org/licenses/MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/v1/systems/", include("systems.api.v1.urls")),
    path("api/v1/measurements/", include("measurements.api.v1.urls")),
]

if settings.DEBUG and not is_running_tests():
    import debug_toolbar

    urlpatterns = [
        path("__silk__/", include("silk.urls", namespace="silk")),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

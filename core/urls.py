from django.contrib import admin
from django.urls import path, include

from core import settings
from core.settings import is_running_tests

urlpatterns = [
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
else:
    urlpatterns = [
        path("__silk__/", include("silk.urls", namespace="silk")),
    ] + urlpatterns

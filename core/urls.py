from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("systems.urls")),
    path("api/measurements/", include("measurements.urls")),
    path("", include("auth_app.urls")),
]

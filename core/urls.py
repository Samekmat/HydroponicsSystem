from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/v1/systems/", include("systems.api.v1.urls")),
    path("api/v1/measurements/", include("measurements.api.v1.urls")),
]

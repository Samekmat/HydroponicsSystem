from django.urls import path, include
from rest_framework.routers import DefaultRouter

from systems.views import HydroponicsSystemViewSet


router = DefaultRouter()
router.register(r"systems", HydroponicsSystemViewSet, basename="system")

urlpatterns = [
    path("", include(router.urls)),
]

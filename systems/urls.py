from django.urls import path
from systems.views import HydroponicsSystemListCreate, HydroponicsSystemDetail

urlpatterns = [
    path("systems/", HydroponicsSystemListCreate.as_view(), name="system-list-create"),
    path("systems/<int:pk>/", HydroponicsSystemDetail.as_view(), name="system-detail"),
]

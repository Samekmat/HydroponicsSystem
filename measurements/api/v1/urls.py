from django.urls import path
from measurements.api.v1.views import MeasurementListCreate

urlpatterns = [
    path("", MeasurementListCreate.as_view(), name="measurement-list-create"),
]

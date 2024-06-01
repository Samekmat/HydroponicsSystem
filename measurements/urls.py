from django.urls import path
from measurements.views import MeasurementListCreate

urlpatterns = [
    path("", MeasurementListCreate.as_view(), name="measurement-list-create"),
]

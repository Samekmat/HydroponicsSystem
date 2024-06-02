from typing import Type

import django_filters
from measurements.models import Measurement


class MeasurementFilter(django_filters.FilterSet):
    measured_at = django_filters.DateTimeFromToRangeFilter()
    pH_data = django_filters.RangeFilter()
    water_temperature = django_filters.RangeFilter()
    TDS = django_filters.RangeFilter()

    class Meta:
        model: Type[Measurement] = Measurement
        fields: list[str] = ["system", "measured_at", "pH_data", "water_temperature", "TDS"]

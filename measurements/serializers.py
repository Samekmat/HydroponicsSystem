from typing import Type

from rest_framework import serializers
from measurements.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[Measurement] = Measurement
        fields: list[str] = ["id", "system", "pH_data", "water_temperature", "TDS", "measured_at"]
        read_only_fields: list[str] = ["measured_at"]

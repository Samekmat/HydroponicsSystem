from rest_framework import serializers
from measurements.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id", "system", "pH_data", "water_temperature", "TDS", "measured_at"]
        read_only_fields = ["measured_at"]

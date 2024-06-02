from rest_framework import serializers

from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer
from systems.models import HydroponicsSystem


class HydroponicsSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description"]
        read_only_fields = ["owner", "created_at", "updated_at"]


class HydroponicsSystemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description", "measurements"]
        read_only_fields = ["owner", "created_at", "updated_at"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        last_10_measurements = Measurement.objects.filter(system=instance).order_by(
            "-measured_at"
        )[:10]
        representation["measurements"] = MeasurementSerializer(
            last_10_measurements, many=True
        ).data
        return representation

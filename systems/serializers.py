from rest_framework import serializers

from measurements.serializers import MeasurementSerializer
from systems.models import HydroponicsSystem


class HydroponicsSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description"]
        read_only_fields = ["owner", "created_at", "updated_at"]


class HydroponicsSystemDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description", "measurements"]
        read_only_fields = ["owner", "created_at", "updated_at"]

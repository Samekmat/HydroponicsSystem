from typing import Type

from django.db.models import QuerySet
from rest_framework import serializers

from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer
from systems.models import HydroponicsSystem


class HydroponicsSystemSerializer(serializers.ModelSerializer[HydroponicsSystem]):
    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description"]
        read_only_fields = ["owner", "created_at", "updated_at"]


class HydroponicsSystemDetailSerializer(serializers.ModelSerializer[HydroponicsSystem]):
    class Meta:
        model: Type[HydroponicsSystem] = HydroponicsSystem
        fields: list[str] = ["owner", "name", "description", "measurements"]
        read_only_fields: list[str] = ["owner", "created_at", "updated_at"]

    def to_representation(self, instance: HydroponicsSystem) -> dict:
        representation: dict = super().to_representation(instance)
        last_10_measurements: QuerySet[Measurement] = Measurement.objects.filter(
            system=instance
        ).order_by("-measured_at")[:10]
        representation["measurements"] = MeasurementSerializer(
            last_10_measurements, many=True
        ).data
        return representation

from rest_framework import serializers
from systems.models import HydroponicsSystem


class HydroponicsSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicsSystem
        fields = ["owner", "name", "description"]
        read_only_fields = ["owner"]

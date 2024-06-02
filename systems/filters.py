import django_filters
from systems.models import HydroponicsSystem


class HydroponicsSystemFilter(django_filters.FilterSet):
    class Meta:
        model = HydroponicsSystem
        fields = ["name", "created_at", "updated_at"]

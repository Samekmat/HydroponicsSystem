from typing import Type

import django_filters
from systems.models import HydroponicsSystem


class HydroponicsSystemFilter(django_filters.FilterSet):
    class Meta:
        model: Type[HydroponicsSystem] = HydroponicsSystem
        fields: list[str] = ["name", "created_at", "updated_at"]

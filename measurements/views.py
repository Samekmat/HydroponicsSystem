from typing import Type, List, Any, Iterable, Union, Optional

from django.contrib.auth.models import AnonymousUser, User
from django.db.models import QuerySet
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.serializers import BaseSerializer

from measurements.filters import MeasurementFilter
from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer
from systems.models import HydroponicsSystem


class MeasurementListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve list of measurements or create a new measurement.

    - GET: Returns a list of all measurements for the authenticated user.
    - POST: Creates a new measurement for the authenticated user's hydroponics system.

    Attributes:
    queryset (QuerySet): The queryset to retrieve measurements from the database.
    serializer_class (Serializer): The serializer class used to validate and deserialize input,
     and serialize output.
    permission_classes (list): List of permission classes that control access to this view.

    Methods:
    perform_create(self, serializer):
        Custom method to associate the measurement with the hydroponics system
         owned by the authenticated user.
        Ensures that the system ID provided in the request data belongs
         to the authenticated user before saving.

    get_queryset(self):
        Returns:
            QuerySet: A queryset filtered to include only measurements belonging
             to the authenticated user's systems.
    """

    queryset: QuerySet[Measurement] = Measurement.objects.all()
    serializer_class: Type[MeasurementSerializer] = MeasurementSerializer
    permission_classes: List[Type[permissions.BasePermission]] = [permissions.IsAuthenticated]
    filter_backends: List[Type[DjangoFilterBackend]] = [DjangoFilterBackend, OrderingFilter]
    filterset_class: Type[MeasurementFilter] = MeasurementFilter
    ordering_fields: Iterable[str] = ["measured_at", "pH_data", "water_temperature", "TDS"]

    def perform_create(self, serializer: BaseSerializer[Any]) -> None:
        """
        Associates the measurement with a hydroponics system owned by the authenticated user.

        Args:
            serializer (Serializer): The serializer instance containing validated data.

        Raises:
            Http404: If the system does not belong to the authenticated user.
        """
        system_id: Optional[Union[str, int]] = self.request.data.get("system")

        if system_id is None:
            raise Http404("System ID must be provided")

        try:
            system_id = int(system_id)
        except (ValueError, TypeError):
            raise Http404("System ID must be a valid integer")

        user: Union[User, AnonymousUser] = self.request.user

        if not isinstance(user, User):
            raise Http404("User must be authenticated")

        system = HydroponicsSystem.objects.get(id=system_id, owner=user)
        serializer.save(system=system)

    def get_queryset(self) -> QuerySet[Measurement]:
        """
        Filters the queryset to include only measurements belonging to the authenticated user.

        Returns:
            QuerySet: A queryset filtered by the authenticated user's hydroponics systems.
        """
        return self.queryset.filter(system__owner=self.request.user)

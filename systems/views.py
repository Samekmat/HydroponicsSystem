from typing import Union, Type

from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter

from systems.filters import HydroponicsSystemFilter
from systems.models import HydroponicsSystem
from systems.serializers import HydroponicsSystemSerializer, HydroponicsSystemDetailSerializer


class HydroponicsSystemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing HydroponicsSystem instances.

    This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Users must be authenticated to interact with the HydroponicsSystem instances.
    """

    queryset = HydroponicsSystem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HydroponicsSystemFilter
    ordering_fields = ["name", "created_at", "updated_at"]

    def get_serializer_class(
        self,
    ) -> Union[Type[HydroponicsSystemSerializer], Type[HydroponicsSystemDetailSerializer]]:
        """
        Return appropriate serializer class based on action.
        """
        if self.action == "retrieve":
            return HydroponicsSystemDetailSerializer
        return HydroponicsSystemSerializer

    def get_queryset(self) -> QuerySet[HydroponicsSystem]:
        """
        Restricts the returned HydroponicsSystem instances to those owned by the current user.

        Returns:
            QuerySet[HydroponicsSystem]: A queryset of HydroponicsSystem instances filtered by
             the current authenticated user.
        """
        return HydroponicsSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: HydroponicsSystemSerializer) -> None:
        """
        Sets the owner of the HydroponicsSystem instance
         to the current authenticated user upon creation.

        Args:
            serializer (HydroponicsSystemSerializer): The serializer instance to save.
        """
        serializer.save(owner=self.request.user)

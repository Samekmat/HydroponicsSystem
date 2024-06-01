from rest_framework import permissions, viewsets
from systems.models import HydroponicsSystem
from systems.serializers import HydroponicsSystemSerializer


class HydroponicsSystemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing HydroponicsSystem instances.

    This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Users must be authenticated to interact with the HydroponicsSystem instances.
    """

    queryset = HydroponicsSystem.objects.all()
    serializer_class = HydroponicsSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Restricts the returned HydroponicsSystem instances to those owned by the current user.

        Returns:
            QuerySet: A queryset of HydroponicsSystem instances filtered by
             the current authenticated user.
        """
        return HydroponicsSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Sets the owner of the HydroponicsSystem instance
         to the current authenticated user upon creation.

        Args:
            serializer (HydroponicsSystemSerializer): The serializer instance to save.
        """
        serializer.save(owner=self.request.user)

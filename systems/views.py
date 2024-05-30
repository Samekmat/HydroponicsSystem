from rest_framework import generics, permissions
from systems.models import HydroponicsSystem
from systems.serializers import HydroponicsSystemSerializer


class HydroponicsSystemListCreate(generics.ListCreateAPIView):
    queryset = HydroponicsSystem.objects.all()
    serializer_class = HydroponicsSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HydroponicsSystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HydroponicsSystem.objects.all()
    serializer_class = HydroponicsSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.owner)

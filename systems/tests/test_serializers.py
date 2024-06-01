from django.test import TestCase
from systems.serializers import HydroponicsSystemSerializer
from systems.factories import HydroponicsSystemFactory


class HydroponicsSystemSerializerTest(TestCase):
    def test_serializer(self):
        system = HydroponicsSystemFactory()
        serializer = HydroponicsSystemSerializer(system)
        data = serializer.data
        self.assertEqual(data["name"], system.name)
        self.assertEqual(data["description"], system.description)
        self.assertEqual(data["owner"], system.owner.id)

    def test_serializer_validation(self):
        system = HydroponicsSystemFactory.build()
        data = {"name": system.name, "description": system.description, "owner": system.owner.id}
        serializer = HydroponicsSystemSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], system.name)

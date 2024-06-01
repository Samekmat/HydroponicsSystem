from django.test import TestCase
from rest_framework.renderers import JSONRenderer

from measurements.factories import MeasurementFactory
from measurements.serializers import MeasurementSerializer


class MeasurementSerializerTestCase(TestCase):
    def test_measurement_serializer(self):
        measurement = MeasurementFactory()

        serializer = MeasurementSerializer(measurement)

        serialized_data = JSONRenderer().render(serializer.data)

        self.assertIn(b'"system"', serialized_data)
        self.assertIn(b'"pH_data"', serialized_data)
        self.assertIn(b'"water_temperature"', serialized_data)
        self.assertIn(b'"TDS"', serialized_data)

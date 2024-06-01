from django.test import TestCase
from measurements.factories import MeasurementFactory
from measurements.models import Measurement


class FactoryTests(TestCase):
    def test_measurement_factory(self):
        measurement = MeasurementFactory()
        self.assertIsInstance(measurement, Measurement)
        self.assertTrue(measurement.system)
        self.assertTrue(measurement.pH_data)
        self.assertTrue(measurement.water_temperature)
        self.assertTrue(measurement.TDS)
        self.assertEqual(Measurement.objects.count(), 1)

    def test_measurement_batch_creation(self):
        num_measurements = 5
        measurements = MeasurementFactory.create_batch(num_measurements)

        self.assertEqual(len(measurements), num_measurements)
        for user in measurements:
            self.assertIsInstance(user, Measurement)

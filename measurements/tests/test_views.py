from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from measurements.models import Measurement
from measurements.factories import MeasurementFactory
from systems.factories import UserFactory, HydroponicsSystemFactory


class MeasurementListCreateTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.system = HydroponicsSystemFactory(owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.url = reverse("measurement-list-create")

    def test_get_measurements_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_measurements(self):
        MeasurementFactory.create_batch(2, system=self.system)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_measurements_unauthorized(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_measurement(self):
        data = {"system": self.system.id, "pH_data": 6.0, "water_temperature": 25.0, "TDS": 600.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Measurement.objects.count(), 1)

    def test_create_measurement_invalid_ph(self):
        data = {"system": self.system.id, "pH_data": 15.0, "water_temperature": 25.0, "TDS": 600.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_measurement_invalid_water_temperature(self):
        data = {"system": self.system.id, "pH_data": 6.0, "water_temperature": 50.0, "TDS": 600.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_measurement_invalid_tds(self):
        data = {"system": self.system.id, "pH_data": 6.0, "water_temperature": 25.0, "TDS": 2500.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_measurement_invalid_system(self):
        data = {"system": 999, "pH_data": 6.0, "water_temperature": 25.0, "TDS": 600.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_measurement_unauthorized(self):
        self.client.logout()
        data = {"system": self.system.id, "pH_data": 6.0, "water_temperature": 25.0, "TDS": 600.0}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

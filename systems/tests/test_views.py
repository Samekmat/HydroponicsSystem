from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from auth_app.factories import UserFactory
from systems.factories import HydroponicsSystemFactory
from systems.models import HydroponicsSystem


class HydroponicsSystemViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = AccessToken.for_user(self.user)
        self.system = HydroponicsSystemFactory(owner=self.user)

    def test_list_hydroponics_systems(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_create_hydroponics_system(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "New System", "description": "A new hydroponics system"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HydroponicsSystem.objects.count(), 2)
        self.assertEqual(HydroponicsSystem.objects.last().name, "New System")

    def test_retrieve_hydroponics_system(self):
        url = reverse("system-detail", args=[self.system.id])
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.system.name)

    def test_update_hydroponics_system(self):
        url = reverse("system-detail", args=[self.system.id])
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "Updated System", "description": self.system.description}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.system.refresh_from_db()
        self.assertEqual(self.system.name, "Updated System")

    def test_delete_hydroponics_system(self):
        url = reverse("system-detail", args=[self.system.id])
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HydroponicsSystem.objects.count(), 0)

    def test_list_hydroponics_systems_unauthenticated(self):
        url = reverse("system-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_hydroponics_system_unauthenticated(self):
        url = reverse("system-list")
        data = {"name": "New System", "description": "A new hydroponics system"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_hydroponics_system_unauthenticated(self):
        url = reverse("system-detail", args=[self.system.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_hydroponics_system_unauthorized(self):
        other_user = UserFactory()
        other_system = HydroponicsSystemFactory(owner=other_user)
        url = reverse("system-detail", args=[other_system.id])
        data = {"name": "Updated System", "description": other_system.description}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_hydroponics_system_unauthorized(self):
        other_user = UserFactory()
        other_system = HydroponicsSystemFactory(owner=other_user)
        url = reverse("system-detail", args=[other_system.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_hydroponics_system_empty_name(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "", "description": "A hydroponics system with an empty name"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(HydroponicsSystem.objects.count(), 1)

    def test_create_hydroponics_system_empty_description(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "Empty Description System", "description": ""}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(HydroponicsSystem.objects.count(), 1)

    def test_create_hydroponics_system_maximum_length_name(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "A" * 64, "description": "A system with a maximum length name"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HydroponicsSystem.objects.count(), 2)

    def test_create_hydroponics_system_exceeded_name_length(self):
        url = reverse("system-list")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))
        data = {"name": "A" * 65, "description": "A description exceeding the maximum length"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(HydroponicsSystem.objects.count(), 1)

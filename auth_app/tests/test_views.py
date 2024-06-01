from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class RegisterViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("auth-register")

    def test_register_view_creates_user(self):
        url = reverse("auth-register")
        data = {"username": "test_user", "password": "test_password", "email": "test@example.com"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="test_user").exists())

    def test_register_view_invalid_data(self):
        url = reverse("auth-register")
        data = {"username": "", "password": "", "email": "invalid_email"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

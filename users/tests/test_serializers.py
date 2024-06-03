from rest_framework.test import APITestCase

from users.serializers import UserSerializer


class UserSerializerTestCase(APITestCase):
    def test_user_serializer_valid_data(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid_data(self):
        data = {
            "username": "testuser",
            "email": "invalidemail",
            "password": "password123",
        }
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())

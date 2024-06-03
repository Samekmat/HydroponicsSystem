from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class TestAuthAppUrls(SimpleTestCase):
    def test_token_obtain_pair_url_resolves(self):
        url = reverse("token-obtain-pair")
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh_url_resolves(self):
        url = reverse("token-refresh")
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_register_url_resolves(self):
        url = reverse("auth-register")
        self.assertEqual(resolve(url).func.view_class, RegisterView)

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from systems.views import HydroponicsSystemViewSet


class UrlsTest(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("system-list")
        self.assertEqual(resolve(url).func.cls, HydroponicsSystemViewSet)

    def test_detail_url_resolves(self):
        url = reverse("system-detail", args=[1])
        self.assertEqual(resolve(url).func.cls, HydroponicsSystemViewSet)

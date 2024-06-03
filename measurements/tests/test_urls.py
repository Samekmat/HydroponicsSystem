from django.test import SimpleTestCase
from django.urls import reverse, resolve

from measurements.api.v1.views import MeasurementListCreate


class MeasurementUrlTest(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("measurement-list-create")
        self.assertEqual(resolve(url).func.cls, MeasurementListCreate)

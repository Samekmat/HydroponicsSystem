from django.test import TestCase
from systems.factories import UserFactory, HydroponicsSystemFactory
from django.contrib.auth.models import User
from systems.models import HydroponicsSystem


class HydroponicsSystemFactoryTest(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsInstance(user, User)
        self.assertTrue(user.username)
        self.assertTrue(user.check_password("password123"))

    def test_hydroponics_system_factory(self):
        system = HydroponicsSystemFactory()
        self.assertIsInstance(system, HydroponicsSystem)
        self.assertTrue(system.name)
        self.assertTrue(system.description)
        self.assertIsInstance(system.owner, User)

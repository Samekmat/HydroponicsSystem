from django.test import TestCase
from systems.factories import UserFactory, HydroponicsSystemFactory
from django.contrib.auth.models import User
from systems.models import HydroponicsSystem


class HydroponicsSystemFactoryTest(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsInstance(user, User)
        self.assertTrue(user.username)
        self.assertTrue(user.password)
        self.assertEqual(User.objects.count(), 1)

    def test_hydroponics_system_factory(self):
        system = HydroponicsSystemFactory()
        self.assertIsInstance(system, HydroponicsSystem)
        self.assertTrue(system.name)
        self.assertTrue(system.description)
        self.assertIsInstance(system.owner, User)
        self.assertEqual(HydroponicsSystem.objects.count(), 1)

    def test_user_batch_creation(self):
        num_users = 5
        users = UserFactory.create_batch(num_users)

        self.assertEqual(len(users), num_users)
        for user in users:
            self.assertIsInstance(user, User)

    def test_systems_batch_creation(self):
        num_systems = 3
        systems = HydroponicsSystemFactory.create_batch(num_systems)

        self.assertEqual(len(systems), num_systems)
        for system in systems:
            self.assertIsInstance(system, HydroponicsSystem)

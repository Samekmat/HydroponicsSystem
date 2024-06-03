from django.test import TestCase
from systems.factories import UserFactory
from django.contrib.auth.models import User


class UserFactoryTest(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsInstance(user, User)
        self.assertTrue(user.username)
        self.assertTrue(user.password)
        self.assertEqual(User.objects.count(), 1)

    def test_user_batch_creation(self):
        num_users = 5
        users = UserFactory.create_batch(num_users)

        self.assertEqual(len(users), num_users)
        for user in users:
            self.assertIsInstance(user, User)

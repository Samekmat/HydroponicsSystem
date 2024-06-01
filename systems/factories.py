import factory
from django.contrib.auth.models import User
from systems.models import HydroponicsSystem


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password123")


class HydroponicsSystemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HydroponicsSystem

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    description = factory.Faker("text")

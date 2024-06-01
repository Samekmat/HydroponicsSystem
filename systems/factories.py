import factory

from systems.models import HydroponicsSystem

from auth_app.factories import UserFactory


class HydroponicsSystemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HydroponicsSystem

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    description = factory.Faker("text")

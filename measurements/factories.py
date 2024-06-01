import factory
from measurements.models import Measurement

from systems.factories import HydroponicsSystemFactory


class MeasurementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Measurement

    system = factory.SubFactory(HydroponicsSystemFactory)

    pH_data = factory.Faker(
        "pydecimal", left_digits=1, right_digits=2, positive=True, min_value=0, max_value=14
    )

    water_temperature = factory.Faker(
        "pydecimal", left_digits=2, right_digits=2, positive=True, min_value=0, max_value=45
    )

    TDS = factory.Faker(
        "pydecimal", left_digits=3, right_digits=2, positive=True, min_value=0, max_value=2000
    )

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from systems.models import HydroponicsSystem


class Measurement(models.Model):
    system = models.ForeignKey(
        HydroponicsSystem,
        related_name="measurements",
        on_delete=models.CASCADE,
        help_text="The hydroponics system associated with this measurement.",
    )

    pH_data = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(14)],
        help_text="The pH level of the nutrient solution, should be between 0 and 14.",
    )

    water_temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(45)],
        help_text="The water temperature in Celsius, should be between 0°C and 45°C.",
    )

    TDS = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(2000)],
        help_text="The Total Dissolved Solids (TDS) in ppm, should be between 0 and 2000 ppm.",
    )

    measured_at = models.DateTimeField(
        auto_now_add=True, help_text="The date and time this measurement was taken."
    )

    def __str__(self) -> str:
        return f"Measurement for {self.system} at {self.measured_at}"

    class Meta:
        ordering: list[str] = ["-measured_at"]

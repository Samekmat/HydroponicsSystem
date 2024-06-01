# Generated by Django 5.0.6 on 2024-06-01 12:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("systems", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="hydroponicssystem",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hydroponicssystem",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="hydroponicssystem",
            name="owner",
            field=models.ForeignKey(
                help_text="Owner of the system.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="systems",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

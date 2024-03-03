# Generated by Django 4.2.9 on 2024-03-03 16:09

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djstripe", "0012_2_8"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("kind", models.IntegerField(choices=[(0, "Fiscal"), (1, "Participation")])),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonationTier",
            fields=[
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("recurrence", models.IntegerField(choices=[(0, "month"), (1, "year")])),
                (
                    "stripe_price",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="djstripe.price",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]

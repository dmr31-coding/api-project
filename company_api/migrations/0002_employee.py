# Generated by Django 5.0.3 on 2024-03-19 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=20)),
                ("about", models.TextField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Manager", "manager"),
                            ("Software Developer", "sd"),
                            ("Project Leader", "pl"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company_api.company",
                    ),
                ),
            ],
        ),
    ]
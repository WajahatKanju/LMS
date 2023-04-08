# Generated by Django 4.1.7 on 2023-04-08 19:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Class", "0001_initial"),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SchoolClasses",
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
                ("active", models.BooleanField(default=True)),
                (
                    "pass_percentage",
                    models.FloatField(
                        default=33.3,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Class.class"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schools",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30, unique=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "classes",
                    models.ManyToManyField(
                        through="school.SchoolClasses", to="Class.class"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="schoolclasses",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school.schools"
            ),
        ),
        migrations.CreateModel(
            name="ClassSubject",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.employee"
                    ),
                ),
                (
                    "school_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school.schoolclasses",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.subject"
                    ),
                ),
            ],
        ),
    ]

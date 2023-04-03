# Generated by Django 4.1.7 on 2023-04-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_schools_employees"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schools",
            name="employees",
        ),
        migrations.AlterField(
            model_name="employee",
            name="designation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.schools"
            ),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="class_position",
        ),
        migrations.AlterField(
            model_name="student",
            name="dob",
            field=models.DateField(blank=True, default="1900-01-01"),
        ),
    ]
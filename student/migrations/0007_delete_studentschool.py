# Generated by Django 4.1.7 on 2023-04-05 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_student_grade"),
    ]

    operations = [
        migrations.DeleteModel(
            name="StudentSchool",
        ),
    ]
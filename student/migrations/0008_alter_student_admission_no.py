# Generated by Django 4.1.7 on 2023-04-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0007_delete_studentschool"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="admission_no",
            field=models.IntegerField(
                default=models.IntegerField(primary_key=True, serialize=False),
                unique=True,
            ),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-03 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
        ("main", "0010_alter_employee_designation_alter_marks_class_subject_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="school",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="school.schools",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="employee",
            name="designation",
            field=models.CharField(max_length=30),
        ),
    ]
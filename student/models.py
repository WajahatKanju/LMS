from datetime import datetime

from django.db import models
from django.urls import reverse


class Student(models.Model):
    status_choices = [('Active', 'Active'), ('Struck off', 'Struck off'), ('Graduated', 'Graduated')]
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]

    roll_no = models.IntegerField(editable=True, blank=False, primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default='1900-01-01', blank=True)

    gender = models.CharField(max_length=10, choices=gender_choices)

    admission_no = models.IntegerField(default=roll_no, unique=True)
    admission_date = models.DateField(default=datetime.now)
    student_cnic = models.CharField(max_length=15, unique=True)
    father_cnic = models.CharField(max_length=15)
    grade = models.ForeignKey('school.SchoolClasses', on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=12)
    status = models.CharField(max_length=10, choices=status_choices, default='Active')

    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('student:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('student:delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Position(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_position = models.PositiveIntegerField(blank=True)


class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.ForeignKey('school.SchoolClasses', on_delete=models.CASCADE)

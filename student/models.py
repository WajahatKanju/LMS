from datetime import datetime

from django.db import models
from django.urls import reverse


class Student(models.Model):
    roll_no = models.IntegerField(editable=True, blank=False, primary_key=True)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default='1900-01-01', blank=True)
    admission_no = models.IntegerField(default=roll_no)
    admission_date = models.DateField(default=datetime.now)
    student_cnic = models.CharField(max_length=15)
    father_cnic = models.CharField(max_length=15)
    mobile = models.CharField(max_length=12)
    active = models.BooleanField(default=True)

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


class StudentSchool(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.ForeignKey('school.Schools', on_delete=models.CASCADE)

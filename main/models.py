import uuid
from datetime import datetime
from enum import unique

from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(editable=True, blank=False, primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(default='01/01/1990', blank=True)
    admission_no = models.IntegerField(default=roll_no)
    admission_date = models.DateField(default=datetime.now)
    student_cnic = models.CharField(max_length=20)
    father_cnic = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    class_position = models.PositiveIntegerField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Classes(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Schools(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    classes = models.ManyToManyField(Classes, through='SchoolClasses')

    def __str__(self):
        return f'{self.name}'


class SchoolClasses(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.classes.name} - {self.school.name}'


class ClassSubject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    school_class = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_class.school.name} - {self.subject.name}'


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_subject = models.ForeignKey(ClassSubject, on_delete=models.CASCADE)
    marks = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student.name} - {self.class_subject.subject.name}'
import uuid
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(editable=True, blank=False, primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField(default='01/01/1990', blank=True)
    admission_no = models.IntegerField(default=roll_no)
    admission_date = models.DateField(default=datetime.now)
    student_cnic = models.CharField(max_length=15)
    father_cnic = models.CharField(max_length=15)
    mobile = models.CharField(max_length=12)
    class_position = models.PositiveIntegerField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_position = models.PositiveIntegerField(blank=True)


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Classes(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Schools(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    classes = models.ManyToManyField(Classes, through='SchoolClasses')

    def __str__(self):
        return f'{self.name}'


class SchoolClasses(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    pass_percentage = models.FloatField(default=33.3, validators=[MinValueValidator(0), MaxValueValidator(100)])

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


class Settings(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    selected_school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    selected_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student_changes = models.BooleanField(default=False)
    batch_marks_changes = models.BooleanField(default=False)
    single_marks_changes = models.BooleanField(default=False)
    subject_changes = models.BooleanField(default=True)
    marks_lock_changes = models.BooleanField(default=True)

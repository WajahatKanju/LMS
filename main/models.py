import uuid
from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    school = models.ForeignKey('school.Schools', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Marks(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    class_subject = models.ForeignKey('school.ClassSubject', on_delete=models.CASCADE)
    marks = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student.name} - {self.class_subject.subject.name}'


class Settings(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    selected_school = models.ForeignKey('school.Schools', on_delete=models.CASCADE)
    selected_class = models.ForeignKey('Class.Class', on_delete=models.CASCADE)
    student_changes = models.BooleanField(default=False)
    batch_marks_changes = models.BooleanField(default=False)
    single_marks_changes = models.BooleanField(default=False)
    subject_changes = models.BooleanField(default=True)
    marks_lock_changes = models.BooleanField(default=True)

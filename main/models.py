import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser
from school.models import Schools

from .managers import CustomUserManager

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Marks(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    class_subject = models.ForeignKey('school.ClassSubject', on_delete=models.CASCADE)
    marks = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student.name} - {self.class_subject.subject.name}'


class User(AbstractUser):
    designation = models.CharField(max_length=30)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, blank=True, related_name='main_users')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='main_users',
        verbose_name=_('user permissions'),
        help_text=_(
            'Specific permissions for this user.'
            'Note: This only affects permissions checked by the "has_permission" method on models.'
        ),
    )

    objects =  CustomUserManager()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Employee'


class ClassSubject(models.Model):
    title = models.CharField(max_length=50)
    grade = models.ForeignKey('Class.Class', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='class_subjects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ClassSubject'
